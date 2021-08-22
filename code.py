# Coptright Pena Superkoodari
# Super Awesome-o Inc.

import pytest
from main import check_psw
from main import check_email
from main import check_psw_equal
from main import check_credentials

#Tests to question 1: -------------------------------
def test_email1():
  email = "pena.superkoodari@SuperAwesome-o.Inc"
  assert check_email(email) is True

def test_check_psw1():
  psw = "PRIVATEcodeDOESnotBELONGtoGITHUB"
  assert check_psw(psw) is True
  

# TODO write the unit tests for the new functions, remove the comment notation and replace assert False with your code: ---------------------------- 
# 1. Test that two equal passwords return true
def test_psw_equal1():
  assert True

# 2. Test that the function is case sensitive
def test_psw_equal2():
  assert True

# 3. Test that two inequal passwords return false
def test_psw_equal3():
  assert True

# 4. Test that two equal passwords in the correct format and a correct email return true
def test_check_credentials1():
  assert True

# 5. Test that two inequal passwords in the correct format and a correct email return false
def test_check_credentials2():
  assert True

# 6. Test that two equal passwords in the correct format and an incorrect email return false
def test_check_credentials3():
  assert True
