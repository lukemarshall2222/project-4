"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
""" 

#import pytest    # Testing framework
import nose
from nose.tools import assert_raises
import arrow
import logging
from acp_times import close_time, open_time
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

TIME1 = '2023-08-05T00:00'
TIME2 = '2025-12-17T14:23' 
TIME3 = '2027-04-27T06:44'

def test_zero():
    start_time = arrow.get(TIME1)
    close = close_time(0, 200, start_time)
    open = open_time(0, 200, start_time)
    assert open == start_time
    assert close == start_time.shift(minutes=60)

def test_ex1_openings():
    start_time = arrow.get(TIME2)
    cont1 = open_time(60, 200, start_time)
    cont2 = open_time(120, 200, start_time)
    cont3 = open_time(175, 200, start_time)
    cont4 = open_time(205, 200, start_time) # also tests control starting beyond 'end' of race
    assert cont1 == start_time.shift(minutes=106)
    assert cont2 == start_time.shift(minutes=212)
    assert cont3 == start_time.shift(minutes=309)
    assert cont4 == start_time.shift(minutes=353)

def test_ex1_closings():
    start_time = arrow.get(TIME2)
    cont1 = close_time(60, 200, start_time)
    cont2 = close_time(120, 200, start_time)
    cont3 = close_time(175, 200, start_time)
    cont4 = close_time(205, 200, start_time) # also tests control starting beyond 'end' of race
    assert cont1 == start_time.shift(minutes=240)
    assert cont2 == start_time.shift(minutes=480)
    assert cont3 == start_time.shift(minutes=700)
    assert cont4 == start_time.shift(minutes=810)

# for pytests (much better)
'''def test_negatives():
    start_time = arrow.get(TIME1)
    with pytest.raises(ValueError) as exec_info:
        open_time(-1, 200, start_time)
    with pytest.raises(ValueError) as exec_info:
        close_time(-1, 200, start_time)'''

def test_negatives():
    start_time = arrow.get(TIME1)
    assert_raises(ValueError, open_time, -1, 200, start_time)
    assert_raises(ValueError, close_time, -1, 200, start_time)

def test_ex2_openings():
    start_time = arrow.get(TIME3)
    cont1 = open_time(100, 600, start_time)
    cont2 = open_time(200, 600, start_time)
    cont3 = open_time(350, 600, start_time)
    cont4 = open_time(550, 600, start_time)
    assert cont1 == start_time.shift(minutes=176)
    assert cont2 == start_time.shift(minutes=353)
    assert cont3 == start_time.shift(minutes=634)
    assert cont4 == start_time.shift(minutes=1028)

def test_ex2_closings():
    start_time = arrow.get(TIME3)
    cont1 = close_time(100, 600, start_time)
    cont2 = close_time(200, 600, start_time)
    cont3 = close_time(350, 600, start_time)
    cont4 = close_time(550, 600, start_time)
    cont5 = close_time(600, 600, start_time)
    assert cont1 == start_time.shift(minutes=400)
    assert cont2 == start_time.shift(minutes=800)
    assert cont3 == start_time.shift(minutes=1400)
    assert cont4 == start_time.shift(minutes=2200)
    assert cont5 == start_time.shift(minutes=2400)

def test_ex3():
    start_time = arrow.get(TIME3)
    cont_open = open_time(890, 1000, start_time)
    cont_close = close_time(890, 1000, start_time)
    assert cont_open == start_time.shift(minutes=1749)
    assert cont_close == start_time.shift(minutes=3923)

def test_grader_ex():
    assert open_time(220, 400, arrow.get("2018-11-17T06:00")).format("YYYY-MM-DDTHH:mm") == arrow.get("2018-11-17T12:30").format("YYYY-MM-DDTHH:mm")

