#!/usr/bin/env python
#coding=utf-8
import sys
sys.path.append('..')
from model import *
from flask import Flask, request, render_template,redirect,make_response,flash,session,g,url_for,jsonify
import os
from PIL import Image
from werkzeug.utils import secure_filename
from flask.ext.sqlalchemy import SQLAlchemy
from os import urandom
import requests
from flask.ext.restful import reqparse, abort, Api, Resource
import json
from time import *
import hashlib
from M2Crypto import util
from Crypto.Cipher import AES
from PIL import Image

IMG_FLODER = 'static/img/'
admin_list=['201632220424','5297459','20164994118']
api = Api(app)


def decrypt(data):
	iv = '9b738aa2ee18145a' # app id
	KEY = '298fe57f669647ffe92ee1deba8b944e' # app secret
	mode = AES.MODE_CBC
	data = util.h2b(data)
	decryptor = AES.new(KEY, mode, IV=iv)
	plain = decryptor.decrypt(data)
	plain = "".join([ plain.strip().rsplit("}" , 1)[0] ,  "}"] )
	oauth_state = json.loads(plain)
	return oauth_state


def hashpw(a):
	ha=hashlib.md5()
	ha.update(a)
	return str(ha.hexdigest())


def IsMobile(a):
	a=a.lower()
	MobileAgent=["iphone", "ipod", "ipad", "android", "mobile", "blackberry", "webos", "incognito", "webmate", "bada", "nokia", "lg", "ucweb", "skyfire"]
	for i in MobileAgent:
		if i in a:
			return True
	else:
		return False


def Thumbnail(fname):
	size=160,160
	im=Image.open(IMG_FLODER+fname)
	im.thumbnail(size,Image.ANTIALIAS)
	im.save(IMG_FLODER+fname+'.thumbnail','png')


class Index(Resource):
	def get(self,page = 1):
		if 'userid' in session and session['userid'] != '':
			LoginVer = False
		else:
			LoginVer = True
		paginate = UserData.query.filter(UserData.Verify==True).order_by(UserData.Id.desc()).paginate(page, 5, False)
		infoes = []
		for i  in paginate.items:
			infoes.append(i.dict())
		return jsonify({'users':infoes,'page':page,'title':u'寻物招领','Login':LoginVer,'IsMobile':IsMobile(request.headers.get('User-Agent'))})


class Login(Resource):
	def get(self):
		if 'userid' in session and session['userid']!='':
			LoginVer = False
		else:
			LoginVer = True
		return {'LoginVer':LoginVer,'IsMobile':IsMobile(request.headers.get('User-Agent'))}

	def post(self):
			if 'userid' in session and session['userid']!='':
				LoginVer = False
			else:
				LoginVer = True
			form=request.form
			p=db.session.query(User).filter(User.EMail==form['EMail']).first()
			LoginStatus = False
			if  p!=None and p.PassWord==hashpw(form['PassWord']):
				session['userid'] = p.UserId
				LoginStatus = True
			return jsonify({'status':LoginStatus,'LoginVer':LoginVer,'IsMobile':IsMobile(request.headers.get('User-Agent'))})


api.add_resource(Index,'/found/<id>')
api.add_resource(Login,'/found/login')

if __name__=='__main__':
	app.run(host='0.0.0.0',port=8888, debug=True)
