# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:39:05 2019

@author: 10060638(heartofrevel)
"""

import win32com.client


def read_doc_file(doc_file_path):
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.visible = False
        word.Documents.Open(doc_file_path)
        doc = word.ActiveDocument
        return doc.Range().Text
    except Exception as e:
        print("Error reading the doc file : "+str(e))
        
    