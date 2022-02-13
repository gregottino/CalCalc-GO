import argparse
import numexpr as ne
import urllib.request
"""
CalCalc is a module to evalute string inputs as mathematical expressions
"""

def calculate(input_str, wolfram_switch):
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
            output_str = urllib.request.urlopen(f'http://api.wolframalpha.com/v2/result?i={url_friendly_input_string}&appid={wolfram_app_id}&format=plaintext').read()
            output_str = output_str = str(output_str, 'utf-8')
        else:
            #if the worlfram flag is off, inform the user that the expression cannot be evaluated with numexpr 
            output_str += " : is not a valid numexpr expression and cannon be evaluated, try with wolfram alpha '-w' flag"
    return output_str
    

def main(parser):
    parser_input = parser.parse_args()
    input_str = parser_input.input_str
    wolfram_switch = parser_input.wolfram_switch
    print(calculate(input_str, wolfram_switch))
    return 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser for CalCalc input')
    parser.add_argument('input_str', help='Input string of mathematical expression, to be evaluated. Arguement should be a simple string or quote enclosed string')
    parser.add_argument('-w', action='store_true', default=False,
                    dest='wolfram_switch',
                    help='Use Wolfram Alpha if an exception is raised by numexpr')
    main(parser)
