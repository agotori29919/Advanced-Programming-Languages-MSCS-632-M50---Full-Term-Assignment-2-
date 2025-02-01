# Python example demonstrating dynamic typing and closures
def make_multiplier(factor):
    def multiplier(number):
        return factor * number  # 'factor' is captured from the outer scope
    return multiplier

double = make_multiplier(2)
print("Double of 5 is", double(5))
