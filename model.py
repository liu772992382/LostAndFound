#!/usr/bin/env python
#coding=utf8
from flask import Flask, request, render_template,redirect,make_response,flash,session
import flask
import os
import sys
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'Users'
    Id = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.String(50))
    TrueName = db.Column(db.String(50))
    EMail = db.Column(db.String(64))
    PassWord = db.Column(db.String(50))
    StuNumber = db.Column(db.String(15))
    RegTime = db.Column(db.String(50))

class UserData(db.Model):
    __tablename__ = 'NoticeData'
    UserId = db.Column(db.String(20))
    Id = db.Column(db.Integer,primary_key=True)
    Time = db.Column(db.String(50))
    Header = db.Column(db.String(50))
    Place = db.Column(db.String(100))
    ThingsType = db.Column(db.String(20))
    Type = db.Column(db.String(10))
    Content = db.Column(db.String(400))
    ImgPath = db.Column(db.String(150))
    #ThumbnailPath = db.Column(db.String(150))
    LostStatus = db.Column(db.Boolean,default=True)
    ContactWay = db.Column(db.String(100))
    Verify = db.Column(db.Boolean,default=False)
    SubTime=db.Column(db.String(30))

db.create_all()
