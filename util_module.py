import os
from enum import Enum
import logging
# logging.basicConfig(level=logging.DEBUG)


def generateQuestionHTML(question, options, questionNo):
    list = ['a', 'b', 'c', 'd']
    str = ""
    for index, option in enumerate(options):
        str += f"""
       <div class="option">{list[index]}. {option}</div>
      """
    return f"""
<div class="wrapper">
  <div class="question">
   {questionNo + 1}.  {question}
  </div>
  <div class="options">
    {str}
  </div>
</div>
"""


def generateTheoryQuestion(question, questionNo):
    return f""" <div class="wrapper theory">
        <div class="question">
          {questionNo + 1}.  {question}
        </div>
   </div>

   """


def createHTML(body):
    return f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   <style>
     .container {{
        display: flex;
       flex-direction: column;
       border: 1px solid #CCCCFF;
       width: 100%;
       height: 100%;
       padding: 15px
     }}

     .header {{
     width: 100%;
     height: 30px;
     display: flex;
     justify-content: space-between;

     }}

     img {{
       width: 30px;
       height: auto;
       margin-right: 20px;
     }}


     .wrapper {{
       margin: 10px;
       display: flex;
       flex-direction: column;
     }}

     .question {{
       font-size: 15px;
       font-weight: bold
     }}

     .options {{
       display: flex;
       font-size: 15px;
       justify-content: space-between;
       margin: 10px;
     }}

  </style>
</head>

<body>
    <div class="container">
     <div class="header">
       <div> <img src="fairy.png" alt="fairy image"></img></div>
       <div></div>
        <div>Prachi</div>
      </div>
        {body}
    </div>
</body>
</html>
"""


class QuestionType(Enum):
    OBJECTIVES = "objectives"
    THEORY = "Theory"


class COLUMNS(Enum):
    QUESTION = "Questions"
    OPTIONA = "optionA"
    OPTIONB = "optionB"
    OPTIONC = "optionC"
    OPTIOND = "optionD"
    TYPE = "Type"
