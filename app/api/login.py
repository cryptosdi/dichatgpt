from flask import Flask, request
from app.api import lg


@lg.route('', methods=['POST'])
def login():
    return 'login34567876543'