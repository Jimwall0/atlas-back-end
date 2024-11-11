#!/usr/bin/python3
"""This is file trying to use some rest api"""
from flask import Flask, urllib, requests

app = Flask(__name__)


@app.route("/")
