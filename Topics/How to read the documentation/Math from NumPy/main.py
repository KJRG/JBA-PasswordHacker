# import the required library
import math


def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    cosine = math.cos(math.radians(angle_in_degrees))
    print(round(cosine, 2))
