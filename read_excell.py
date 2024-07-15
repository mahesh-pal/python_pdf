import pandas as pd
from util_module import generateQuestionHTML, createHTML, generateTheoryQuestion, COLUMNS, QuestionType
from weasyprint import HTML, CSS
import os

current_directory = os.getcwd()

file_path = 'worksheet_gen.xlsx'
output_path = 'output.pdf'
try:
    data = pd.read_excel(file_path,)
    itr = data.iterrows()
    html = ""
    body = ''
    for index, row in itr:
        question = row[COLUMNS.QUESTION.value]
        type = row[COLUMNS.TYPE.value]
        if (type == QuestionType.OBJECTIVES.value):
            optionA = row[COLUMNS.OPTIONA.value]
            optionB = row[COLUMNS.OPTIONB.value]
            optionC = row[COLUMNS.OPTIONC.value]
            optionD = row[COLUMNS.OPTIOND.value]
            body += generateQuestionHTML(question,
                                         [optionA, optionB, optionC, optionD], index)

        if (type == QuestionType.THEORY.value):
            body += generateTheoryQuestion(question, index)
    html = createHTML(body)
    # print(html)
    HTML(string=html, base_url=current_directory).write_pdf(output_path)

except Exception as e:
    traceback.print_exc()
