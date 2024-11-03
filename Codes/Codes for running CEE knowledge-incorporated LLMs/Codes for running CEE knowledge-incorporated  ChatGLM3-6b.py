                                                                                                                       from transformers import AutoTokenizer, AutoModel
import os


tokenizer = AutoTokenizer.from_pretrained("/root/autodl-tmp/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("/root/autodl-tmp/chatglm3-6b", trust_remote_code=True).half().cuda()
model = model.eval()



messages = []
import pandas as pd
import re
import os
import csv
from bs4 import BeautifulSoup
import pandas as pd
#from docx import Document
import uuid
import pandas as pd
import openpyxl


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
  # for answer in correct_answers:
  individual_correct_answers = split_correct_answers(correct_answers)
  for individual_answer in individual_correct_answers:
    if individual_answer in str(answers_from_model):
      correct_ones = correct_ones + 1
    if individual_answer not in str(answers_from_model):
      missed_ones = missed_ones + 1
  wrong_answers = set(["A", "B", "C", "D", "E"]).difference(correct_answers)
  #print("wrong_answers", wrong_answers)
  for individual_wrong_answer in wrong_answers:
    if individual_wrong_answer in str(answers_from_model):
      wrong_ones = wrong_ones + 1

  if wrong_ones == 0:
    if missed_ones == 0:
      score = 2
    else:
      score = min(correct_ones * 0.5, 2)
  #print("correct_ones,wrong_ones,missed_ones", correct_ones, wrong_ones, missed_ones)
  return score

def read_excel_column(file_path, sheet_name, column_name):
  # 读取Excel文件
  df = pd.read_excel(file_path, sheet_name=sheet_name)

  # 提取指定列的数据，转换为列表返回
  column_data = df[column_name].tolist()

  return column_data



years=["1Z101010","1Z101020","1Z101030","1Z101040","1Z101050","1Z101060","1Z101070","1Z102010","1Z102020","1Z102030","1Z102040","1Z102050","1Z102060","1Z102070","1Z102080","1Z103010","1Z103020","1Z103030","1Z103040","1Z103050","1Z103060","1Z103070","1Z103080","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"]
for year in years:
  print("Code of the examination",year)
  Questions=read_excel_column(year+".xlsx", "Sheet1", "augmented_prompt")
  Answers=read_excel_column(year+".xlsx", "Sheet1", "答案")
  #print(Questions)
  df = pd.DataFrame(columns=["Question","Correct_Answer",'Answer1', "Score1"])
  # for Question in Questions
  #   print
  for i in range(len(Questions)):

    message=Questions[i]


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
    
    history=[]
    answers_from_model,history = model.chat(tokenizer, Questions[i],history=[])


    answer1=answers_from_model

    
    # df2 = pd.DataFrame([
    # {"Question":Questions[i],"Correct_Answer":Answers[i],"Answer1":answer1,"Score1":final_score(Questions[i],answer1,Answers[i]),"Answer2":response_text_davinci_003.choices[0].text,"Score2":final_score(Questions[i],answer2,Answers[i])}])
    df2 = pd.DataFrame([
    {"Question":Questions[i],"Correct_Answer":Answers[i],"Answer1":answer1,"Score1":final_score(Questions[i],answer1,Answers[i])}])

    # print("No Question",i+1,"\n","Right_Answer:",Answers[i],"\n"+"Answer_from_text_davinci_003:",answer1.strip().replace("\n",""),"\nAnswer_from_:GPT3.5Turbo",answer2.strip().replace("\n",""),"\nAnswer_from_GPT4:",answer3.strip().replace("\n",""))
    print("No Question",i+1,"\n","Right_Answer:",Answers[i],"\nAnswer_from_original_chatglm3-6b:",answer1.strip().replace("\n",""))

    df = pd.concat([df, df2], axis=0)

  save_df_to_excel(df, "Answers_from_knowledge_Chatglm3_6B_EE_"+year+".xlsx", "sheet1")
    #reply = response2["choices"][0]["message"]["content"]
    #print(row)


        
