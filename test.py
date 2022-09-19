import os, psycopg2
from discord.ext import commands

DATABASE_URL = os.environ["postgres://gczlpwwvbsyxqb:e764f473c897aade574e643c7320db02ada1528c926ad0f56535d47d67110f0b@ec2-174-129-253-47.compute-1.amazonaws.com:5432/dcktac0i33t53g"]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

print(input())
