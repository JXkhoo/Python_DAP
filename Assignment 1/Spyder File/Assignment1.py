# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:22:04 2020

@author: MR.COOL
"""

data_list = []  
total_date = []
sales_list ={}

def calculate_daily_sale(data_list):
    #To get the total number of dates and put them in a list
    for index in range(len(data_list)):
        if data_list[index]['date'] not in total_date:
            total_date.append(data_list[index]['date'])
    
    result ={}
    
    for number in range(len(total_date)):
        
        total_sales_A = total_sales_B = total_sales_C = total_sales_D = total_sales_E = total_sales_F  = 0

        for index in range(len(data_list)):
            
            #if the current date in data_list same as total_date, it will proceed and find out which item it is and calculate it
            if data_list[index]['date'] == total_date[number]:
                if data_list[index]['item'] == 'Item_A':
                    day_sales_A = data_list[index]['amount']*data_list[index]['price']
                    total_sales_A = round(total_sales_A + day_sales_A,2)
                    
                elif data_list[index]['item'] == 'Item_B':
                    day_sales_B = data_list[index]['amount']*data_list[index]['price']
                    total_sales_B = round(total_sales_B + day_sales_B,2)
                    
                elif data_list[index]['item'] == 'Item_C':
                    day_sales_C = data_list[index]['amount']*data_list[index]['price']
                    total_sales_C = round(total_sales_C + day_sales_C,2)
                    sales_list = {total_date[number]:{'Item_C':total_sales_C}}
                    
                elif data_list[index]['item'] == 'Item_D':
                    day_sales_D = data_list[index]['amount']*data_list[index]['price']
                    total_sales_D = round(total_sales_D + day_sales_D,2)
                    sales_list = {total_date[number]:{'Item_D':total_sales_D}}
                    
                elif data_list[index]['item'] == 'Item_E':
                    day_sales_E = data_list[index]['amount']*data_list[index]['price']
                    total_sales_E = round(total_sales_E + day_sales_E,2)
                    sales_list = {total_date[number]:{'Item_E':total_sales_E}}
                    
                elif data_list[index]['item'] == 'Item_F':
                    day_sales_F = data_list[index]['amount']*data_list[index]['price']
                    total_sales_F = round(total_sales_F + day_sales_F,2)
                    sales_list = {total_date[number]:{'Item_F':total_sales_F}}
                    
                else:
                    print("This item is not found")
                
                #result will be update with the sales of each item on that day
                result.update({total_date[number]:{'Item_A':total_sales_A,'Item_B':total_sales_B,'Item_C':total_sales_C,'Item_D':total_sales_D,'Item_E':total_sales_E,'Item_F':total_sales_F}})

    return result


def get_total_sale(result_list):
    for index in range(len(data_list)):
        if data_list[index]['date'] not in total_date:
            total_date.append(data_list[index]['date'])
            
    total_sales_A = total_sales_B = total_sales_C = total_sales_D = total_sales_E = total_sales_F  = 0
       
    for num_of_date in range(len(total_date)):
        total_sales_A = round(total_sales_A + result[total_date[num_of_date]]['Item_A'],2)
        total_sales_B = round(total_sales_B + result[total_date[num_of_date]]['Item_B'],2)
        total_sales_C = round(total_sales_C + result[total_date[num_of_date]]['Item_C'],2)
        total_sales_D = round(total_sales_D + result[total_date[num_of_date]]['Item_D'],2)
        total_sales_E = round(total_sales_E + result[total_date[num_of_date]]['Item_E'],2)
        total_sales_F = round(total_sales_F + result[total_date[num_of_date]]['Item_F'],2)
    
    total_sales={'Item_A':total_sales_A,'Item_B':total_sales_B,'Item_C':total_sales_C,'Item_D':total_sales_D,'Item_E':total_sales_E,'Item_F':total_sales_F}
    return total_sales
  

#To read the text file    
with open('data_assignment_1.txt') as openfileobject:
    index = 0
    
    #For each line in the text file, it is splited and stored in a list called data list
    for line in openfileobject:
        word = line.split()
        date_list = word[0]
        item_name = word[1]
        amount_sold = int(word[2])
        price_per_unit = float(word[3])
        file_data = {'date':date_list,'item':item_name,'amount':amount_sold,'price':price_per_unit}
        data_list.append(file_data)

result = calculate_daily_sale(data_list)  
print(result['2020-09-29']['Item_A'])
print(result['2020-09-29'])
total_sales = get_total_sale(result)
print('\nTotal sales of each item throughout the period\n',total_sales)


        
        
        
            
          
