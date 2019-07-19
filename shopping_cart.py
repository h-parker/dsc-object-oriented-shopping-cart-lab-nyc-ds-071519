import math

class ShoppingCart:
    # write your code here
    def __init__(self, total=0, items={}, emp_discount=None):
        self.total = float(total)
        self.items = items
        self.employee_discount = emp_discount
        self.last_item = None
    
    
    def add_item(self, name, price, quantity=1):
        self.total += int(quantity)*float(price)
        
        # dictionary should add item as new if it's not there
        if name not in list(self.items.keys()):
            self.items[name] = {'price': float(price), 
                                'quantity': int(quantity)}
        
        # if it's not new, it should only update the quantity
        else:
            self.items[name]['quantity'] += quantity
            
        self.last_item = {'name': name, 
                          'price': price, 
                          'quantity': int(quantity)}
                        
        return self.total

    def repeated_price_list(self):
        # need to list prices that repeat due to having more than one in 
        # your cart so stats are accurate
        total_items = [] # store all prices, repeated for each quantity
        
        for item in self.items:
            i = 0
            #adds each item the number of times stored in 'quantity'
            while i < self.items.get(item)['quantity']:
                total_items.append(self.items.get(item)['price']) #adds price
                i += 1
        return total_items
        
    def mean_item_price(self):
        # get list with repetitions of price to reflect quantity of each
        # item in the basket
        total_items = self.repeated_price_list()
        return sum(total_items)/len(total_items)

    def median_item_price(self):
        total_items = self.repeated_price_list()
        dataLen = len(total_items)
        
        #if length is odd, take middle value, by dividing the length by 2, 
        #then rounding up
        if (dataLen % 2) == 1:
            return total_items[round(dataLen/2)]
        
        #if the length is even, take the mean of the middle two values, which
        #have indices length/2 and (length/2 + 1)
        elif (dataLen % 2) == 0:
            #remember that indices are indexed at 0
            return math.mean([total_items[int(dataLen/2-1)], 
                                     total_items[int(dataLen/2)]]
                                    ) 

    def apply_discount(self):
        if self.employee_discount == None:
            return "Sorry, there is no discount to apply to your cart :( "
        else:
            return self.total*(1 - self.employee_discount*.01)

    def void_last_item(self):
        # if nothing has been added
        if self.last_item == None:
            return "There are no items in your cart!"
        
        # if there is at least one item in the cart
        else:
            # update total by subtracting price of item last added, multiplied
            # by the quantity added, from the total
            
            print(self.total)
            print(self.items.get(self.last_item['name'])['price']*self.last_item['quantity'])
            self.total -= self.items.get(self.last_item['name'])['price']*self.last_item['quantity']
            
            # update the item entry by subtracting quantity last added from
            # the current quantity listed in the items list
            
            # new quantity calculation
            new_quantity = self.items.get(self.last_item['name'])['quantity'] - self.last_item['quantity']
            
            # updating the quantity entry in the items list
            self.items[self.last_item['name']] = {'price': self.last_item['price'],
                                                  'quantity': new_quantity
                                                  }
            
            # if there's no more of that item in the cart, delete the whole
            # item from the items entry
            if self.items[self.last_item['name']].get('quantity') == 0:
                self.items.pop(self.last_item['name']) 
                
            return
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    