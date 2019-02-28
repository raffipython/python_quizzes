import argparse 

class Bike():                                                   
    """ Comments """
    def __init__(self, size_var, model_var, price_var): 
        self.size  = size_var
        self.model = model_var
        self.price = price_var
        if price_var >= 1000:
            self.msg = "Too pricy! Ask Santa"
        else:
            self.msg = "Let us go to the bike shop!"

    @staticmethod
    def bike_type(size): #[Note: no self is being passed] 
        if size >= 25:
            return "Adults bike"
        else:
            return "Kids bike"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(""" Generic Log Watcher """)
    parser.add_argument("-s", "--size", type=int, help="Bike size")
    parser.add_argument("-m", "--model", type=str, help="Bike model")
    parser.add_argument("-p", "--price", type=int, help="Bike price")
    parser.add_argument("-w", "--women", help="Is the bike women's bike?", action="store_true")
    
    args = parser.parse_args()
    b = Bike(args.size, args.model, args.price)
    print("Bikes")
    print("Size  is {}".format(b.size))    
    print("Model is {}".format(b.model))    
    print("Price is {}".format(b.price))    
    print("Msg   is {}".format(b.msg))    
    print("Type  is {}".format(b.bike_type(b.size)))    
    if args.women:
        print("It is also a women bike")
