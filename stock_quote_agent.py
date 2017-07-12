#!/usr/local/bin python

'''
  Simple script reads list of stock quote of the day and prints on screen
  their quotes now
  Input: list of stock Symbols
'''


import sys
#import types, os, ast, getopt
#import datetime as dt
import pandas_datareader.data as web


class QuoteAgent(object):
    '''
       Reads stock quote symbol as string
       and fetches for quote price and prints it out

    '''
    def __init__(self, symbol):
        
        self.symbol = symbol # list of symbols


    def print_quote(self):
        
        stock_quote = web.get_quote_yahoo(self.symbol)
 
        print(stock_quote)



## Main progrom 

def main(argv):
    
#    arg_dict = {}  # Argument parsed dictionary
#    # Might run Program as --> python stock_quote_agent.py --l = '[AAPL, AMZN, GOOG, MSFT]'
#    
#    parses = {'li':list, 'di':dict, 'tu':tuple} ## type of command line object passed
#    
#    singles = ''.join(x[0]+':' for x in parses)
#    
#    long_form = [x+'=' for x in parses]
#    
#    d = {x[0] + ':':'--' + x for x in parses}
#    
#    try:
#        
#        opts, args = getopt.getopt(argv, singles, long_form)
#        
#    except getopt.GetoptError:
#        
#        print("Bad Input Arguments")
#        
#        sys.exit(2)
#        
#    for opt, arg in opts:
#        
#        if opt[1] + ':' in d:
#            
#            o = d[opt[1] + ':'][2:]
#            
#        elif opt in d.values(): 
#            
#            o = opt[2:]
#        
#        else: o = ''
#        
#        print(opt, arg, o)
#        
#        if o and arg:
#            
#            arg_dict[o] = ast.literal_eval(arg)
#            
#        if not o or not isinstance(arg_dict[o], parses[o]):
#            
#            print(opt, arg, "Error: Bad Arg")
#            
#            sys.exit(2)
#            
#    ## print the type of argument object passed at command line
#    for e in arg_dict:
#        
#        print(e, arg_dict[e], type(arg_dict[e]) )
        
    
            
   # Main agent stuff
    try:
        #create stock quotes agents 
        stock_symbols = []
         
        for symbol in sys.argv[1:]:
        
            stock_symbols.append(str(symbol))
            
        
        qAgent= QuoteAgent(stock_symbols)
        
        #print stock quotes
        qAgent.print_quote()
    
    except:
    
        print("Error: Provide at least one Stock Symbol")


         
## Run Program
         
'''
  Run at command line as follows:
  e.g 
  --> python stock_quote_agent.py  AAPL, AMZN, GOOG, MSFT, TSLA, FB, PYPL, BABA
'''
         
         
if __name__ == '__main__':
    
    main(sys.argv[1:])
         




