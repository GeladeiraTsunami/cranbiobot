#Yahoo finance API: http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=USDINR=X

#Google finance API: https://finance.google.com/bctzjpnsun/converter?a=$amount&from=$from_Currency&to=$to_Currency

#Google currency codes: https://developers.google.com/adsense/management/appendix/currencies

# ex msg: 230 eur to brl

message = "230 eur to brl"

def converterFunc(message):
    data = message.split()

    float(user_value) = data[1] 
    user_tag = data[2]
    to_tag = data[4]

    response = requests.get("http://free.currencyconverterapi.com/api/v5/convert?q=EUR_USD&compact=y")

    print(response.status_code)

    rate = response.status_code

    #rate =  conversion using the api
    float(converted) = user_value * rate

    print ("{0:.3f} {} = {0:.3f} {}".format(user_value, user_tag, converted, to_tag))