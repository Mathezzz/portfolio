from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint


bp = Blueprint('portfolio',__name__)

@bp.route('/')
def home():
    return render_template('home.html', codes=session.keys())

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/projetos')
def projetos():
    return render_template('projetos.html')