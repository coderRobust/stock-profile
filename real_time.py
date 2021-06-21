
import datetime
from collections import Counter

start_time="09:30:00" 
START_TIME=datetime.datetime.strptime(start_time, "%H:%M:%S")
end_time="16:30:00" 
END_TIME=datetime.datetime.strptime(end_time, "%H:%M:%S")

def real_time_feed():
    
    word_list = []
    hasmap = {}
    with open('stock_data.txt', 'r') as fobj:
        digit = next(fobj)
        val = [x.strip() for x in fobj.readlines()]
        for ele in val:
            curr_list = ele.split(',')
            curr_time= datetime.datetime.strptime(curr_list[1], "%H:%M:%S")
            if curr_time >= START_TIME and curr_time <= END_TIME:
                if curr_list[0] not in hasmap:
                    hasmap[curr_list[0]] = [] 
                    hasmap[curr_list[0]].append(curr_list[1:])
                else:
                    hasmap[curr_list[0]].append(curr_list[1:])

    for key, value in hasmap.items():
    # function to display real time feed of a part
        show_real_data_a({key:value})
    # function to display real time feed of b part
        show_real_data_b({key:value})

    
def show_real_data_a(hasmap):
  for key, value in hasmap.items():
        list_time = []
        active_symbol = []
        prices = []
        for ele in value:
            list_time.append(ele[0])
            active_symbol.append(ele[1])
            prices.append(ele[2])
        symbol = Counter(active_symbol)
        active_hour = []
        for ele in list_time:
            hour = ele.split(':')[0] 
            active_hour.append(hour)
        active_hour = Counter(active_hour)
        print(f'Trading Day - {key}')
        print(f'Last Quote Time = {max(list_time)}') 
        print(f'Number of valid quotes = {len(active_symbol)}') 
        print(f'Most active hour = {active_hour.most_common(1)[0][0]}') 
        print(f'Most active symbol = {symbol.most_common(1)[0][0]}')

def show_real_data_b(hasmap):
    map = {}
    for key, value in hasmap.items():
        for ele in value:
            val = ele[1]
            if val not in map:
                map[val] = {'date': None, 'time':[], 'price':[]}
                map[val]['date'] = key
                map[val]['time'].append(ele[0])
                map[val]['price'].append(ele[2])
            else:
                map[val]['time'].append(ele[0])
                map[val]['price'].append(ele[2])

        for key, value in map.items():
            print(f'{value["date"]} {max(value["time"])},{key},{max(value["price"])},{min(value["price"])}')


if __name__ =='__main__':
    # calling function to execute real time feed
    real_time_feed()