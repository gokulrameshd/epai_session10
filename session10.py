
#importing packages
from faker import  Faker
from collections import namedtuple  
import datetime
from datetime import date 
from decimal import Decimal
import numpy as np
import statistics
import random


fake = Faker()

def calculateAge(birthDate): 
    '''
    This functions helps to calculate the age from given date to present date.
    '''
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 


def get_named_tuple(population):
    '''
    This function generates list of fake person details.
    Attributes : 'name','blood_type','current_location','DOB'
    '''
    info_list = []
    person = namedtuple('person',['name','blood_type','current_location','DOB']) 
    for i in range(population):
        profile =  fake.profile()
        p = person(profile['name'],profile['blood_group'],profile['current_location'],profile['birthdate'])
        info_list.append(p)
    return info_list

def named_tuple2dict_list(named_tuple_list):
    """
    This function helps to convert named tuples to dictionaries
    """
    dict_list = []
    for i in named_tuple_list:
        dict_list.append(dict(i._asdict()))
    return dict_list

def cal_mean_current_location(name_tuple_list):
    """
    This function returns the mean current location.
    """
    lan = []
    lon = []
    for i in name_tuple_list:
        lan.append(i.current_location)
        lon.append(i.current_location)
    return np.mean(lan),np.mean(lon)

def named_tuple_cal(named_tuple_list):
    '''
    This function calculates and returns the largest blood type, mean-current_location,
     oldest_person_age ,average age and time taken for calculation using named tuple.
    '''
    t0 = datetime.datetime.now()
    lan = []
    lon = []
    age = []
    blood_group = []
    for i in named_tuple_list:
        lan.append(i.current_location[0])
        lon.append(i.current_location[1])
        age.append(calculateAge(i.DOB))
        blood_group.append(i.blood_type)
    result = statistics.mode(blood_group),(np.mean(lan),np.mean(lon)),np.max(age),np.mean(age)
    t1 = datetime.datetime.now()
    print(f'Time taken for claculation{t1-t0}')
    return result , t1-t0

def dict_cal(dict_list):
    '''
    This function calculates and returns the largest blood type, mean-current_location,
     oldest_person_age ,average age and time taken for calculation using Dictionary.
    '''
    t0 = datetime.datetime.now()
    lan = []
    lon = []
    age = []
    blood_group = []
    for i in dict_list:
        lan.append(i['current_location'][0])
        lon.append(i['current_location'][1])
        age.append(calculateAge(i['DOB']))
        blood_group.append(i['blood_type'])
    result = statistics.mode(blood_group), (np.mean(lan),np.mean(lon)),np.max(age),np.mean(age)
    t1 = datetime.datetime.now()
    print(f'Time taken for claculation{t1-t0}')
    return result,t1-t0

def get_symbol(com_name,i):
    """
    This function returns the symbol for given company name
    """
    symbol = str(i)
    for c in com_name:
        symbol += '_' + c[0]
    return symbol

def get_random_weights():
    """
    This function return random weights in range of 0 to 100.
    """
    return random.uniform(0,100) 

def get_random_open():
    """
    This function return the random open values 
    """
    return round((random.uniform(300,1000)),2)

def get_high(open_value):
    """
    This function calculates the high value
    """
    return round(open_value*(random.uniform(1,3.0)),3)

def get_close(high_value):
    """
    This is function returns the close value
    """
    return round(high_value*(random.uniform(0.2,1.2)),3)

def create_fake_companies_list(no_of_companies):
    """
    This function generates list of fake companies with following attributes,
    'com_name', "symbol", 'open_value', 'high_value', 'close_value','weight'
    """
    company = namedtuple('company',['com_name', "symbol", 'open_value', 'high_value', 'close_value','weight'])
    companies_list = []
    weight_list = []
    for i in range(no_of_companies):
        com_name = fake.company()
        symbol = get_symbol(com_name,i)
        weight = get_random_weights()
        open_value = get_random_open()
        high_value = get_high(open_value)
        close_value = get_close(high_value)
        companies_list.append(company(com_name,symbol, open_value, high_value, close_value ,weight))
        weight_list.append(weight)
    return companies_list,weight_list

def get_stockmarket_points(companies_list,weight_list):
    '''
    This function calculates the stock markets opening point , highest point , closing point.
    The points are calculated by multiplying the values with the normalized weights and summing up all the values.
    '''
    open_points = []
    high_points = []
    close_points = []
    sum_weight = sum(weight_list)
    for com in companies_list:
        open_point = com.open_value * com.weight/sum_weight
        high_point = com.high_value * com.weight/sum_weight
        close_point = com.close_value * com.weight/sum_weight
        open_points.append(open_point)
        high_points.append(high_point)
        close_points.append(close_point)
    return round(sum(open_points),2),round(sum(high_points),2),round(sum(close_points),2)
