class duo:
    ''' class to represent duodecimal numbers 
     
     0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , X , E
     
    Input:
    ------
        either string (base12) or float/int (base10)
        
    http://www.dozenal.org/drupal/sites_bck/default/files/DSA-ConversionRules_0.pdf
    '''
    
    def __init__(self,number):
        ''' determine type of input and convert to decimal/duodecimal '''
        
        self.duo_digits = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 
                  6: '6', 7: '7', 8: '8', 9: '9', 10: 'X', 11: 'E'}
        self.dec_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                  '6': 6, '7': 7, '8': 8, '9': 9, 'E': 11, 'X': 10}
        self.base = 12
        
        if type(number) == int or type(number) == float:
            self.decimal    = number
            self.duodecimal = self.dec_to_duo(number)
        
        elif type(number) == str:
            self.decimal    = self.duo_to_dec(number)
            self.duodecimal = number
        else:
            raise TypeError('unkown type')
      
    def dec_to_duo(self,number):
        ''' convert decimal float/int to duodecimal string '''

        # handle negative numbers
        if number <0:
            number = abs(number)
            sign = '-'
        else:
            sign = ''
        integer, fractional = divmod(number,1)
        
        out = []
        quotient = integer
        while quotient != 0:
            quotient, remainder = divmod(quotient,self.base)
            out.insert(0,remainder)
        integer = ''.join([self.duo_digits[dig] for dig in out])

        if fractional:
            out = []
            remainder = fractional 
            for i in range(len(str(fractional).split('.')[1])+1):
                quotient, remainder = divmod(remainder*self.base,1)
                out.append(quotient)
            if remainder > 0.5:
                out.append(1)
            decimal = '.' + ''.join([self.duo_digits[dig] for dig in out])
        else:
            decimal = ''
            
        return sign + integer + decimal.rstrip('0')

    def duo_to_dec(self,string):
        ''' convert duodecimal string to decimal float/int '''
        
        # handle negative numbers
        if string.startswith('-'):
            string = string[1:]
            sign = -1
        else:
            sign = 1
            
        if set(string) > set('123456789XE'):
            invalid = set(string) - set('123456789XE')
            raise ValueError('invalid character'.format(invalid))
        
        if '.' in string:
            integer, fractional = string.split('.')
        else:
            integer, fractional = string, ''
        
        out = 0
        for power, digit in enumerate(integer[::-1]):
            out += self.dec_digits[digit] * self.base**power
        for power, digit in enumerate(str(fractional),1):
            out += self.dec_digits[digit] * self.base**(-power)
            
        return out
    
    def __add__(self,other):
        '''add two duodecimal numbers'''
        
        if isinstance(other, duo):
            result = self.decimal + other.decimal
        elif type(other) == int or type(other) == float:
            result = self.decimal + other           
        elif type(other) == str:
            result = self.decimal + self.duo_to_dec(other)
        else:
            raise TypeError('unkown type')
        return duo(result)

    def __sub__(self,other):
        ''' subtract two duodecimal numbers '''
        
        if isinstance(other, duo):
            result = self.decimal - other.decimal
        elif type(other) == int or type(other) == float:
            result = self.decimal - other           
        elif type(other) == str:
            result = self.decimal - self.duo_to_dec(other)
        else:
            raise TypeError('unkown type')
        return duo(result)
    
    def __mul__(self,other):
        ''' multiply two duodecimal numbers '''
        
        if isinstance(other, duo):
            result = self.decimal * other.decimal
        elif type(other) == int or type(other) == float:
            result = self.decimal * other           
        elif type(other) == str:
            result = self.decimal * self.duo_to_dec(other)
        else:
            raise TypeError('unkown type')
        return duo(result)
    
    def __truediv__(self,other):
        ''' divide two duodecimal numbers '''
        
        if isinstance(other, duo):
            result = self.decimal / other.decimal
        elif type(other) == int or type(other) == float:
            result = self.decimal / other           
        elif type(other) == str:
            result = self.decimal / self.duo_to_dec(other)
        else:
            raise TypeError('unkown type')
        return duo(result)
    
    def dec(self):
        ''' return the decimal representation '''
        return self.decimal
    
    def __repr__(self):
        return self.duodecimal[:7].rstrip('0') + '(base12)'
    
    def __str__(self):
        return self.duodecimal