__author__ = 'joefalkson'

#using ystockquote library
import ystockquote

'''We have two methods, eval_stock (scores tickers) and store_ticker (takes a csv file of tickers and
stores values into an array'''



##Function designed to evaluate a ticker
def eval_stock(ticker):
    result = "Summary: "
    score = 0
    momentum = False
    if ystockquote.get_50_sma(ticker) > ystockquote.get_200_sma(ticker):
        result+="stock has momentum, 50 day moving avg is %s and 200 day is %s" % (ystockquote.get_50_sma(ticker),
        ystockquote.get_200_sma(ticker))
        score+=1
        momentum=True
    else:
        result+="Stock has no momentum, 50 day moving avg is %s and 200 day is %s" % (ystockquote.get_50_sma(ticker),
        ystockquote.get_200_sma(ticker))

    if float(ystockquote.get_1_year_target(ticker)) > (1.2 * float(ystockquote.get_todays_high(ticker))):
        result+=" 20% away from price target"
        score += 1

    #Short ratio of 5 or higher with positive momentum means investors may likely buy to cover soon
    if momentum==True and float(ystockquote.get_short_ratio(ticker)) > 3.0:
        score+=2

    result+= " \n short ratio is " + ystockquote.get_short_ratio(ticker)

    if float(ystockquote.get_eps(ticker))>.02*float(ystockquote.get_todays_high(ticker)):
        score+=1.5

    result += " \n EPS: " + ystockquote.get_eps(ticker) + " today's high is " + ystockquote.get_todays_high(ticker)

    result+= " \n , notes (if applicable)" + ystockquote.get_notes(ticker)
    return result, "Score is " + str(score)


#tickers taken from http://investexcel.net/all-yahoo-finance-stock-tickers/
##Here we store the tickers from a csv file into an array.
def store_tickers(ticker_file):
    tickers=[]
    with open(ticker_file, "r") as my_file:
        lines=my_file.readlines()

    for line in lines:
        #get rid of the new line syntax
        line=line.strip("',/\n[]")
        tickers.append(line)

    return tickers

print(store_tickers("tickers.csv"))



print (eval_stock('CSG'))

print (type(float(ystockquote.get_todays_high('GOOG'))))

print(ystockquote.get_short_ratio('LQMT'))


print(ystockquote.get_eps_estimate_current_year('GOOG'))
#trailing 12 months number
print(ystockquote.get_eps('GOOG'))
print(ystockquote.get_price_eps_estimate_current_year('GOOG'))



##Some of the methods available
name = ystockquote.get_company_name('GOOG')

mktcap = ystockquote.get_market_cap('GOOG')

print ("Name: %s , Market Cap %s" %(name,mktcap))

ystockquote.get_200_sma()
ystockquote.get_50_sma()
ystockquote.get_annualized_gain()
ystockquote.get_1_year_target()
ystockquote.get_52_week_high()
ystockquote.get_52_week_low()
ystockquote.get_change_200_sma()
ystockquote.get_52_week_range()
ystockquote.get_book_value()
ystockquote.get_eps_estimate_current_year()
ystockquote.get_eps()
ystockquote.get_ticker_trend()
ystockquote.get_short_ratio()
ystockquote.get_revenue()
ystockquote.get_average_daily_volume()
ystockquote.get_float_shares()
ystockquote.get_dividend_yield()
ystockquote.get_notes()
ystockquote.get_pe()
ystockquote.get_all()

print (ystockquote.get_all('GOOG'))