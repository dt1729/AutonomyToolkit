import openai, os, re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import json
import shutil
import numpy as np
import docstring_parser

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

from colorama import Fore, Style
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from statistics import mode
from queue import Queue
from lxml import etree
from parse import parse
from abc import ABC
from comment_parser import comment_parser
from bs4 import BeautifulSoup
from pathlib import Path


class textBot(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.API_KEY            =  os.environ['OPENAI_API_KEY']
        self.docstringParser    =  docstring_parser.google.GoogleParser()
        self.memory             =  ConversationBufferMemory()
        self.llm                =  ChatOpenAI(model='gpt-3.5-turbo')
        self.conversation       =  ConversationChain(
                                        llm=self.llm,
                                        memory=self.memory
                                        )
        self.nodes_logs         =  None

    def chatBot(self):
        pass