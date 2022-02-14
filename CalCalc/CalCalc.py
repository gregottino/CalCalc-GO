import argparse
import numexpr as ne
import urllib.request
"""
CalCalc is a module to evalute string inputs as mathematical expressions
"""

# a dictionary for number terms that may appear in wolfram strings
number_dict = {"ten"      : 10.,
                  "hundred"  : 100.,
                  "thousand" : 1000.,
                  "million"  : 1.0e6,
                  "billion"  : 1.0e9,
                  "trillion" : 1.0e12,
                  "quadrillion" : 1.0e15,}

def calculate(input_str, wolfram_switch=False):
    #wolfram app ID used for non numerical input to CalCalc
    wolfram_app_id = "Q9WVLK-X59R32T65P"
    
    #string to return
    output_str = input_str
    
    #if the string can be evaluted by numexpr, then do so
    try:
        output_str = ne.evaluate(input_str)
    #if numexpr fails, see if wolfram output was desired
    except:
        # if wolfram output is desired, query the API for an answer and print it
        if wolfram_switch:
            #put the query into html format
            url_friendly_input_string = urllib.parse.quote_plus(input_str)
            # open the URL and parse it
            try:
                output_str = urllib.request.urlopen(f'http://api.wolframalpha.com/v2/result?i={url_friendly_input_string}&appid={wolfram_app_id}&format=plaintext').read()
                output_str = output_str = str(output_str, 'utf-8')
            except:
                output_str = "unreadable input by wolfram, please reformat"
        else:
            #if the worlfram flag is off, inform the user that the expression cannot be evaluated with numexpr 
            output_str += " : is not a valid numexpr expression and cannon be evaluated, try with wolfram alpha '-w' flag"
    return output_str
    

def get_wolfram_output_as_float(input_str):
    """Translates a text answer into a floating point number"""
    #split string into chunks by whitespace
    input_split = input_str.split()
    
    if input_split[0] == "about":
        if "times" in input_str and "to the" in input_str:
            return float(input_split[1]) * 10 ** float(input_split[6])
        else:
            # first find weird number words in wolfram and make them floats
            multiplicative_factor = 1.0
            for key in number_dict.keys():
                if key in input_str:
                    multiplicative_factor *= number_dict[key] 
            # return the number times its multipliers
            return float(input_split[1]) * multiplicative_factor
    else:
        return float(input_split[0])
    
    
def test_1():
    """Test if error is handled for junk without wolfram flag"""
    test_str = "some junk"
    assert calculate(test_str,False) == test_str + " : is not a valid numexpr expression and cannon be evaluated, try with wolfram alpha '-w' flag" 

def test_2():
    """Test if error is handled for junk with wolfram flag"""
    test_str = "what the heck is going on here"
    assert calculate(test_str,True) == "unreadable input by wolfram, please reformat"
    
def test_3():
    """Test that a simple calculation of 2+2 returns 4"""
    test_str = "2+2"
    assert calculate(test_str,False) == 4.0
    
def test_4():
    """Check that floating point input works for an answer that returns scientific notation"""
    test_str = "mass of the moon in kg"
    assert get_wolfram_output_as_float(calculate(test_str,True)) == 7.3459e+22
    
    
def test_5():
    """ a test"""
    test_str = "millimeters in a meter"
    assert get_wolfram_output_as_float(calculate(test_str,True)) == 1.0e3
    
    
def main(parser):
    #get the parser object and get the input
    parser_input = parser.parse_args()
    input_str = parser_input.input_str
    wolfram_switch = parser_input.wolfram_switch
    float_switch = parser_input.float_switch
    #print the output from the calculate function using parsed inputs
    calculate_output = calculate(input_str, wolfram_switch)
    
    #convert the output to a float if requested via parser
    if float_switch:
        calculate_output = get_wolfram_output_as_float(calculate_output)
    print(calculate_output)
    return 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser for CalCalc input')
    parser.add_argument('input_str', help='Input string of mathematical expression, to be evaluated. Arguement should be a simple string or quote enclosed string')
    parser.add_argument('-w', action='store_true', default=False,
                    dest='wolfram_switch',
                    help='Use Wolfram Alpha if an exception is raised by numexpr')
    parser.add_argument('-f', action='store_true', default=False,
                    dest='float_switch',
                    help='tore wolframm result as float')
    main(parser)
