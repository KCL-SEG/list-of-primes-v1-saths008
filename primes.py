"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    #if(type(number_of_primes) == int):
        list = []
        list.append(2)
        current_number = 3
        while len(list) < number_of_primes :

            i = 0

            for i in range(0, len(list)):

                if(current_number % list[i] == 0):
                    i = 0
                    current_number+=1
                    break

                elif (not (current_number % list[i] == 0))  and (i == (len(list) -1)):
                    list.append(current_number)







        return(list)

   # else:
   #     print("")
