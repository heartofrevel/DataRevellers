# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:39:05 2019

@author: 10060638(heartofrevel)
"""

import win32com.client
import docx2txt


def read_doc_file(doc_file_path):
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.visible = False
        word.Documents.Open(doc_file_path)
        doc = word.ActiveDocument
        return doc.Range().Text
    except Exception as e:
        print("Error reading the doc file : "+str(e))
    finally:
        word.Application.Quit(-1)
        

def read_docx_file(docx_file_path):
    try:
        result = docx2txt.process(docx_file_path)
        return result
    except Exception as e:
        print("Error reading docx file : "+str(e))
        
        