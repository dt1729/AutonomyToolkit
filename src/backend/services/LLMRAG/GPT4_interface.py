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

    def init_message(self):
        """Creates a message by taking roslogs, from server, errors from execution, 
        and function comments explaining how the code works to the LLM.
        This is version 1 of this function later it will take these, output from GPT 
        and generate a prompt from a smaller LLMs using the previously mentioned 
        """

        self.message = "You're an AI Agent assigned with the job of setting up a robotics simulation environment for the user to play around the test their ideas. \
            To briefly describe the enviornment, you are given a workspace and object files, you're supposed to follow the user's instructions and create a workspace.\
            The simulator/library used here is Drake by MIT. The link is: https://drake.mit.edu/pydrake/index.html"

    def objectAddingPrompt(self, user_input : str) -> str:
        """_summary_

        Args:
            user_input (str): _description_
        """
        
                
        
        pass
    
    def chatBot(self):
        pass
    