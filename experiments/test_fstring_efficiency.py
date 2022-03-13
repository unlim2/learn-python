#!/usr/bin/python3

import time
    
def exec_time(func):
    '''
        Decorator that reports the execution time.
        https://www.geeksforgeeks.org/function-wrappers-in-python/
    '''

    def wrap(*args, **kwargs):
        start = time.time() * 10000000
        result = func(*args, **kwargs)
        end = time.time()  * 10000000
        print(func.__name__, end - start)
        return result
    return wrap

@exec_time
def setup_test_data(count, len):
    '''
        prepare test data and templates for fstrings and format string methods
    '''
    tmpl = "" # template for % operator
    fmts = "" # template for .format metod
    fstr = "" # template for fstring
    data = [] # test data
    for i in range(0, count):
        data.append(" " * len)
        tmpl += "%s"
        fstr += "{data["+str(i)+"]}"
        fmts += "{}"
    return data, tmpl, fmts, fstr

@exec_time
def test_str_plus(data):
    r = ""
    for s in data:
        r += s
    return r

@exec_time
def test_str_percent_operator(data, template):
    return template % tuple(data)

@exec_time
def test_str_format_method(data, template):
    return template.format(*data)

@exec_time
def test_str_fstring_eval(data, template):
    return eval(f'f"{template}"')

@exec_time
def test_str_fstring_10(data):
    return f"{data[0]}{data[1]}{data[2]}{data[3]}{data[4]}{data[5]}{data[6]}{data[7]}{data[8]}{data[9]}"

@exec_time
def test_str_fstring_100(data):
    return f"""{data[0]}{data[1]}{data[2]}{data[3]}{data[4]}{data[5]}{data[6]}{data[7]}{data[8]}{data[9]}
    {data[10]}{data[11]}{data[12]}{data[13]}{data[14]}{data[15]}{data[16]}{data[17]}{data[18]}{data[19]}
    {data[20]}{data[21]}{data[22]}{data[23]}{data[24]}{data[25]}{data[26]}{data[27]}{data[28]}{data[29]}
    {data[30]}{data[31]}{data[32]}{data[33]}{data[34]}{data[35]}{data[36]}{data[37]}{data[38]}{data[39]}
    {data[40]}{data[41]}{data[42]}{data[43]}{data[44]}{data[45]}{data[46]}{data[47]}{data[48]}{data[49]}
    {data[50]}{data[51]}{data[52]}{data[53]}{data[54]}{data[55]}{data[56]}{data[57]}{data[58]}{data[59]}
    {data[60]}{data[61]}{data[62]}{data[63]}{data[64]}{data[65]}{data[66]}{data[67]}{data[68]}{data[69]}
    {data[70]}{data[71]}{data[72]}{data[73]}{data[74]}{data[75]}{data[76]}{data[77]}{data[78]}{data[79]}
    {data[80]}{data[81]}{data[82]}{data[83]}{data[84]}{data[85]}{data[86]}{data[87]}{data[88]}{data[89]}
    {data[90]}{data[91]}{data[92]}{data[93]}{data[94]}{data[95]}{data[96]}{data[97]}{data[98]}{data[99]}"""

@exec_time
def test_function_call(data, template):
    return ""

@exec_time
def test_str_join(data):
    return "".join(data)

def run_test(count, len):
    print("-" * 50)
    print(f"Test joining {count} strings length {len}")
    print("-" * 50)
    data, tmpl, fmts, fstr = setup_test_data(count, len)
    test_function_call(data, tmpl)
    test_str_join(data)
    test_str_plus(data)
    test_str_percent_operator(data, tmpl)
    test_str_format_method(data, fmts)
    test_str_fstring_eval(data, fstr)
    if count == 10: test_str_fstring_10(data)
    if count == 100: test_str_fstring_100(data)
    print("-" * 50)

run_test(10, 1024)
run_test(100, 1024)
run_test(10, 10240)
run_test(100, 10240)
