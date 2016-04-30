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
    id = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.String(50))
    TrueName = db.Column(db.String(50))
    EMail = db.Column(db.String(64))
    PassWord = db.Column(db.String(50))
    StuNumber = db.Column(db.String(15))
    RegTime = db.Column(db.String(50))

    def __str__ (self):
        return "User(Id='%s')" % self.id

    def dict(self):
        return {'Id':self.id,
                'UserId':self.UserId,
                'TrueName':self.TrueName,
                'EMail':self.Email,
                'PassWord':self.PassWord,
                'StuNumber':self.StuNumber,
                'RegTime':self.RegTime}

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

    def dict(self):
    	return {'UserId':self.UserId,
    			'Id':self.Id,
    			'Time':self.Time,
    			'Header':self.Header,
    			'Place':self.Place,
    			'ThingsType':self.ThingsType,
    			'Type':self.Type,
    			'Content':self.Content,
    			'ImgPath':self.ImgPath,
    			'LostStatus':self.LostStatus,
    			'ContactWay':self.ContactWay,
    			'Verify':self.Verify,
    			'SubTime':self.SubTime}
