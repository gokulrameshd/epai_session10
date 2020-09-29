import pytest
from faker import  Faker
from collections import namedtuple  
import datetime
from datetime import date 
from decimal import Decimal
import numpy as np
import statistics
import random
from session10 import *



def test_calculateAge():
    calculated_age = calculateAge(date(1997, 2, 3))
    assert calculated_age == 23 , 'Age calculator is not working!!!!'


# Question 1
def test_get_named_tuple():
    named_tuple_list =  get_named_tuple(10000)
    assert len(named_tuple_list) == 10000 , "Profile not created"

def test_named_tuple2dict_list():
    named_tuple_list =  get_named_tuple(100)
    dict_list = named_tuple2dict_list(named_tuple_list)
    type(dict_list[0]) == type(dict())

# Question 2
def test_nt_vs_dict():
    named_tuple_list = get_named_tuple(population = 10000)
    dict_list = named_tuple2dict_list(named_tuple_list)
    result_1,nt_time_consumption = named_tuple_cal(named_tuple_list)
    result_2,dict_time_consumption = dict_cal(dict_list)
    assert nt_time_consumption < dict_time_consumption , 'nt_time_consumption is high!!!!!!'

# Question 3 
def test_stock_point_gen_cal_nt():
    companies_list,weight_list = create_fake_companies_list(100)
    open_point,high_point,close_point = get_stockmarket_points(companies_list,weight_list)
    assert open_point <= high_point , 'Not working!!'