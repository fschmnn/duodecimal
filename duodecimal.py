class BaseConverter:
    ''' class to represent numbers in diferent bases
     
    Input:
    ------
        numbers : either string (baseX) or float/int (base10)
        digits :string of digits used in the base (e.g. binary: '01')

    Variables:
    ----------
        value : holds the decimal value 
        string : holds the representation in BaseConverter.base 
        
    http://www.dozenal.org/drupal/sites_bck/default/files/DSA-ConversionRules_0.pdf
    '''
    
    def __init__(self,number,digits):
        ''' determine type of input and convert to decimal/duodecimal '''
        
        BaseConverter.digits     = digits
        BaseConverter.base       = len(digits)
        BaseConverter.to_digits = {k: v for k,v in enumerate(digits)}
        BaseConverter.from_digits = {v: k for k,v in enumerate(digits)}
        
        if type(number) == int or type(number) == float:
            self.value  = number
            self.string = BaseConverter.from_dec(number,BaseConverter.base)
        
        elif type(number) == str:
            self.value  = BaseConverter.to_dec(number,BaseConverter.base)
            self.string = number
        else:
            raise TypeError('input type must be str or float/int')
    
    @staticmethod
    def from_dec(number,base):
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
            quotient, remainder = divmod(quotient,base)
            out.insert(0,remainder)
        integer = ''.join([BaseConverter.to_digits[dig] for dig in out])

        if fractional:
            out = []
            remainder = fractional 
            for i in range(len(str(fractional).split('.')[1])+1):
                quotient, remainder = divmod(remainder*base,1)
                out.append(quotient)
            if remainder > 0.5:
                out.append(1)
            decimal = '.' + ''.join([BaseConverter.to_digits[dig] for dig in out])
        else:
            decimal = ''
            
        return sign + integer + decimal.rstrip('0')
   
    @staticmethod
    def to_dec(string,base):
        ''' convert string to decimal float/int '''
        
        # handle negative numbers
        if string.startswith('-'):
            string = string[1:]
            sign = -1
        else:
            sign = 1
            
        if set(string) > set(BaseConverter.digits):
            invalid = set(string) - set(BaseConverter.digits)
            raise ValueError('invalid character'.format(invalid))
        
        if '.' in string:
            integer, fractional = string.split('.')
        else:
            integer, fractional = string, ''
        
        out = 0
        for power, digit in enumerate(integer[::-1]):
            out += BaseConverter.form_digits[digit] * base**power
        for power, digit in enumerate(str(fractional),1):
            out += BaseConverter.from_digits[digit] * base**(-power)
            
        return out
    
    def __add__(self,other):
        if not isinstance(other, BaseConverter):
            other = BaseConverter(other,BaseConverter.digits)

        return BaseConverter(self.value + other.value,BaseConverter.digits)

    def __iadd__(self,other):
        if not isinstance(other, BaseConverter):
            other = BaseConverter(other,BaseConverter.digits)
        self.value = self.value + other.value
        self.string = BaseConverter.from_dec(self.value,BaseConverter.base)

        return self

    def __radd__(self,other):
        return BaseConverter(other,BaseConverter.digits) + self

    def __sub__(self,other):
        if not isinstance(other, BaseConverter):
            other = BaseConverter(other,BaseConverter.digits)

        return BaseConverter(self.value - other.value,BaseConverter.digits)

    def __isub__(self,other):
        if not isinstance(other, BaseConverter):
            other = BaseConverter(other,BaseConverter.digits)
        self.value = self.value - other.value
        self.string = BaseConverter.from_dec(self.value,BaseConverter.base)

        return self

    def __rsub__(self,other):
        return BaseConverter(other,BaseConverter.digits) - self
    
    def __mul__(self,other):
        if not isinstance(other, BaseConverter):
            other = BaseConverter(other,BaseConverter.digits)

        return BaseConverter(self.value * other.value,BaseConverter.digits)

    def __imul__(self,other):
        if not isinstance(other, BaseConverter):
            other = BaseConverter(other,BaseConverter.digits)
        self.value = self.value * other.value
        self.string = BaseConverter.from_dec(self.value,BaseConverter.base)

        return self

    def __rmul__(self,other):
        return BaseConverter(other,BaseConverter.digits) * self

    def __truediv__(self,other):
        if not isinstance(other, BaseConverter):
            other = BaseConverter(other,BaseConverter.digits)

        return BaseConverter(self.value / other.value,BaseConverter.digits)
 
    def __itruediv__(self,other):
        if not isinstance(other, BaseConverter):
            other = BaseConverter(other,BaseConverter.digits)
        self.value = self.value / other.value
        self.string = BaseConverter.from_dec(self.value,BaseConverter.base)

        return self

    def __rtruediv__(self,other):
        return BaseConverter(other,BaseConverter.digits) / self

    def __repr__(self):
        if '.' in self.string: 
            return self.string[:7].rstrip('0') + f'(base{BaseConverter.base})'
        else:
            return self.string + f'(base{BaseConverter.base})'

    def __str__(self):
        return self.string

    def __format__(self,format):
        return self.string

    def decimal(self):
        ''' return the decimal representation '''
        return self.value

    def to_base(self,base):
        ''' give out in different base '''
        return BaseConverter.from_dec(self.value,base) 

class duo(BaseConverter):
    ''' class to represent duodecimal numbers 
     
     0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , X , E
     
    Input:
    ------
        either string (base12) or float/int (base10)
    '''

    def __init__(self,number):
        BaseConverter.__init__(self,number,'0123456789XE')

class binary(BaseConverter):
    def __init__(self,number):
        BaseConverter.__init__(self,number,'01')

class hexa(BaseConverter):
    def __init__(self,number):
        BaseConverter.__init__(self,number,'0123456789ABCDEF')

if __name__ == '__main__':
    a = duo(2)
    a /= 4
    print(a)