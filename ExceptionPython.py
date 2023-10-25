# Exceptions in python

itemsInCart = 0
# Two items will be added to cart


if itemsInCart != 2:
    # raise Exception("Product cart count aren't matching")
    pass

assert (itemsInCart ==0)

#try, catch
try:
    with open('/home/nayana/PycharmProjects/PythonTestProject/filelog.txt', 'r') as reader:
        reader.read()

#except:
 #   print("There is a failure in block")
except Exception as e:
    print(e)

finally:
    print("Cleaning up resources")
