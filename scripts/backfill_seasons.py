from sqlalchemy import create_engine, Table, Column, Integer, Float, String, MetaData
import pandas as pd

df = pd.read_csv('2016-tips.csv')

engine = create_engine('postgresql://clairegatenby@localhost:5432/tipping')