import re
from openai import OpenAI
import openpyxl
import pandas as pd

client = OpenAI(api_key="Your OpenAI's api")

messages = []
import os
import csv
from bs4 import BeautifulSoup
import uuid



def score_of_single_choice(answers_from_model, correct_answer):
  score = 0
  number_of_answers=0
  if correct_answer in str(answers_from_model):
    score = 1
  if "A" in correct_answer:
    number_of_answers=number_of_answers+1
  if "B" in correct_answer:
    number_of_answers=number_of_answers+1
  if "C" in correct_answer:
    number_of_answers=number_of_answers+1
  if "D" in correct_answer:
    number_of_answers=number_of_answers+1
  if number_of_answers>1:
    score=0
  return score



def save_df_to_excel(df, file_path, sheet_name):
  # 创建一个Excel写入器对象
  writer = pd.ExcelWriter(file_path)

  # 将DataFrame写入指定工作表
  df.to_excel(writer, sheet_name=sheet_name, index=False)

  # 保存并关闭Excel文件

  writer.close()
def split_correct_answers(string):
  answer = []
  for character in string:
    answer.append(character)
  return answer


def score_of_multi_choice(answers_from_model, correct_answers):
  score = 0
  correct_ones = 0
  missed_ones = 0
  wrong_ones = 0

  individual_correct_answers = split_correct_answers(correct_answers)
  for individual_answer in individual_correct_answers:
    if individual_answer in str(answers_from_model):
      correct_ones = correct_ones + 1
    if individual_answer not in str(answers_from_model):
      missed_ones = missed_ones + 1
  wrong_answers = set(["A", "B", "C", "D", "E"]).difference(correct_answers)

  for individual_wrong_answer in wrong_answers:
    if individual_wrong_answer in str(answers_from_model):
      wrong_ones = wrong_ones + 1

  if wrong_ones == 0:
    if missed_ones == 0:
      score = 2
    else:
      score = min(correct_ones * 0.5, 2)

  return score

def read_excel_column(file_path, sheet_name, column_name):
  # 读取Excel文件
  df = pd.read_excel(file_path, sheet_name=sheet_name)

  # 提取指定列的数据，转换为列表返回
  column_data = df[column_name].tolist()

  return column_data


years=["2012", "2015", "2014","2016"]
for year in years:
  print("Year",year)
  Questions=read_excel_column(year+".xlsx", "Sheet1", "augmented_prompt")
  Answers=read_excel_column(year+".xlsx", "Sheet1", "答案")
  #print(Questions)
  df = pd.DataFrame(columns=["Question","Correct_Answer",'Answer1', "Score1","Answer2","Score2"])

  for i in range(len(Questions)):

    message=Questions[i]
    messages=[{"role":"user","content": message}]
    response_gpt35turbo=client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages,
      top_p=0,
      temperature =0
    )

    response_gpt4=client.chat.completions.create(
      model="gpt-4",
      messages=messages,
      top_p=0,
      temperature =0
    )


    def final_score(Question,answers_from_model,answers):
      if "四个" in Question:
        score = score_of_single_choice(answers_from_model, answers)
        # total_score = total_score + score
        #print("score of this question & total scores", score, total_score)
      if "五个" in Question:
        score = score_of_multi_choice(answers_from_model, answers)
        # total_score = total_score + score
        #print("score of this question & total scores", score, total_score)
      return score

    answer1=response_gpt35turbo.choices[0].message.content
    answer2=response_gpt4.choices[0].message.content



    df2 = pd.DataFrame([
    {"Question":Questions[i],"Correct_Answer":Answers[i],"Answer1":answer1,"Score1":final_score(Questions[i],answer1,Answers[i]),"Answer2":answer2,"Score2":final_score(Questions[i],answer2,Answers[i])}])

    print("No of Question",i+1,"\n","Right_Answer:",Answers[i],"\nAnswer_from_GPT3.5Turbo:",answer1.strip().replace("\n",""),"\nAnswer_from_GPT4:",answer2.strip().replace("\n",""))

    #df2=pd.DataFrame([['Answer1',response_gpt35turbo["choices"][0]["message"]["content"], response_text_davinci_003.choices[0].text]])

    #row=[response_gpt35turbo["choices"][0]["message"]["content"],response_text_davinci_003.choices[0].text]
    #print (df)
    #print(df2)
    df = pd.concat([df, df2], axis=0)

  save_df_to_excel(df, "All_answers from OpenAI with knowledge"+year+".xlsx", "sheet1")
    #reply = response2["choices"][0]["message"]["content"]
    #print(row)

