import requests
import json
import qianfan
import pandas as pd
import os
import time
chat_comp = qianfan.ChatCompletion(ak="YOUR_API_KEY", sk="YOUR_SECRET_KEY")
os.environ['QIANFAN_AK'] = "YOUR_API_KEY"
os.environ['QIANFAN_SK'] = "YOUR_SECRET_KEY"
def get_access_token():


    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=ewcQGuXT4otZmj5Y3jBFNj5h&client_secret=ouQUt1pt5CfRnjamXQfsGvFqI01D3pBo&grant_type=client_credentials"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")
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
  print("string:", string)
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


def final_score(Question, answers_from_model, answers):
  score=0
  if "四个" in Question:
    score = score_of_single_choice(answers_from_model, answers)
    # total_score = total_score + score
    # print("score of this question & total scores", score, total_score)
  if "五个" in Question:
    score = score_of_multi_choice(answers_from_model, answers)
    # total_score = total_score + score
    # print("score of this question & total scores", score, total_score)
  return score

#years=["-2011", "-2012", "-2013", "-2014", "-2015", "-2016", "-2017", "-2018", "-2019", "-2020",
#       "-2021", "-2022", "-2022.2", "-2023", "1Z201000", "1Z202000", "1Z203000", "1Z204000", "1Z205000",
#       "1Z206000", "1Z207000"]
#years=[-"L2_2023_2","L2_2023","L2_2022","L2_2021","L2_2021_2","L2_2020_2","L2_2020","L2_2019","L2_2018","L2_2017","L2_2016","L2_2015","L2_2014","L2_2013","L2_2012","L2_2011","L1_1Z301000","L1_1Z302000","L1_1Z303000","L1_1Z304000","L1_1Z305000","L1_1Z306000","L1_1Z307000","L1_1Z308000","L2_2Z201000","L2_2Z202000","L2_2Z203000","L2_2Z204000","L2_2Z205000","L2_2Z206000","L2_2Z207000","L2_2Z208000"]
years=["2023"]

for year in years:

  print("Year",year)
  Questions=read_excel_column(year+".xlsx", "Sheet1", "augmented_prompt")
  Answers=read_excel_column(year+".xlsx", "Sheet1", "答案")
  #print(Questions)
  df = pd.DataFrame(columns=["Question","Correct_Answer","Answer1", "Score1","Answer2","Score2","Answer3","Score3","Answer4","Score4"])
  # for Question in Questions
  #   print
  n = 0
  messages = []
  for i in range(len(Questions)):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + str(
          get_access_token())
    #print(i)
  # system_message = input("What type of chatbot you want me to be?")
  # messages.append({"role":"system","content":system_message})
  #print("Alright! I am ready to be your friendly chatbot" + "\n" + "You can now type your messages.")
  #message = input("")
    n=n+1
    message=Questions[i]
    time.sleep(8)

    result_llm_llama_2_13b=chat_comp.do(model="Llama-2-13b-chat", messages=[{
     "role": "user",
    "content": message
     }])

    result_llm_ERNIE_Bot_turbo=chat_comp.do(model="ERNIE-Bot-turbo", messages=[{
    "role": "user",
     "content": message
     }])

    result_llm_ERNIE_Bot_turbo40=chat_comp.do(model="ERNIE-Bot-4", messages=[{
     "role": "user",
     "content": message
     }])


    result_llm_Qianfan_Chinese_Llama_2_7B=chat_comp.do(model="Qianfan-Chinese-Llama-2-7B", messages=[{
     "role": "user",
     "content": message
     }])

    df2 = pd.DataFrame([{"Question": Questions[i], "Correct_Answer": Answers[i],
                          "Answer1": result_llm_llama_2_13b['result'],"Score1": final_score(Questions[i], result_llm_llama_2_13b['result'], Answers[i]),
                          "Answer2": result_llm_ERNIE_Bot_turbo['result'],"Score2": final_score(Questions[i], result_llm_ERNIE_Bot_turbo['result'], Answers[i]),
                          "Answer3": result_llm_ERNIE_Bot_turbo40['result'],"Score3": final_score(Questions[i], result_llm_ERNIE_Bot_turbo40['result'], Answers[i]),
                          "Answer4": result_llm_Qianfan_Chinese_Llama_2_7B['result'],"Score4": final_score(Questions[i], result_llm_Qianfan_Chinese_Llama_2_7B['result'],Answers[i])}])

    print("No of Question", i + 1, "\n", "Right_Answer:", Answers[i],
          "\n" + "Answer_from_llama_2_13b:",
           str(result_llm_llama_2_13b['result']).strip().replace("\n", ""),
           "\n" + "Answer_from_ERNIE_Bot_turbo:",
           str(result_llm_ERNIE_Bot_turbo['result']).strip().replace("\n", ""),
          "\n" + "Answer_from_ERNIE_Bot_turbo40:",
           str(result_llm_ERNIE_Bot_turbo40['result']).strip().replace("\n", ""),
           "\n" + "Answer_from_Qianfan_Chinese_Llama_2_7B:",
           str(result_llm_Qianfan_Chinese_Llama_2_7B['result']).strip().replace("\n", ""))
    df = pd.concat([df, df2], axis=0)
  save_df_to_excel(df, "Answers_from_baidu_with knowledge" + year + ".xlsx", "sheet1"),