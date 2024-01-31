"""
Description: Assignment-4 MyMath Web Application
Author: Azime Ulker
Section Number: 251409
Date Created: January 28,2023

Updates:
"""
import math

class MyMath (): 
    '''This class contains methods for calculating the average and standard deviation of a list of numbers'''   
    
    def __init__(self, *args):
        '''This function initializes the MyMath class'''
        if args:
            self.num_list = list(args)
        else:
            self.num_list = []
            
    def max(self):
        '''This function returns the maximum value in a list of numbers'''
        if self.num_list == []:
            return 0
        
        return max(self.num_list)
    
    def avg(self):
        '''This function calculates the average of a list of numbers'''
        if self.num_list == []:
            return 0  # Average is undefined for an empty list
        
        avg = sum(self.num_list) / len(self.num_list)
        return avg
    
    def stdDev(self):
        '''This function calculates the standard deviation of a list of numbers'''
        if len(self.num_list) < 2:
            return 0  # Sample standard deviation is undefined for a single number
        
        mean = sum(self.num_list) / len(self.num_list)
        squared_diff = [(num - mean) ** 2 for num in self.num_list]
        sample_variance = sum(squared_diff) / (len(self.num_list) - 1)
        sample_std_deviation = math.sqrt(sample_variance)
        
        return sample_std_deviation