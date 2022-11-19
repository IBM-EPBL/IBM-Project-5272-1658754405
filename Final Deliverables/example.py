import re
import numpy as np
import os
from tensorflow import keras
from flask import Flask, app,request,render_template
from tensorflow.keras import models
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.python.ops.gen_array_ops import concat
from keras.applications.inception_v3 import preprocess_input
import requests
from flask import Flask, request, render_template, redirect, url_for
from cloudant.client import Cloudant
def call():
    client = Cloudant.iam('b0981d12-395c-4575-8324-ee850683cbde-bluemix','pI9HWcRnB-QJTEhofMuJplmsmaL1QaLbeVAdw1KLge7o',connect=True)
    my_database = client.create_database('my_data')
    model1 = load_model('Model/level.h5')
    model2 = load_model('Model/body.h5')
    return my_database,model1, model2




