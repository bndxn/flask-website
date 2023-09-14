from flask import Flask, request, jsonify
import numpy as np
import tflite_runtime.interpreter as tflite

app = Flask(__name__)

# Load TFLite model and allocate tensors
interpreter = tflite.Interpreter(model_path="static/converted_model_fused.tflite")
interpreter.allocate_tensors()
