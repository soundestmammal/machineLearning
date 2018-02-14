# -*- coding: utf-8 -*-

# Appendix A Problems 2, 6, 8, 10, 11

# Problem 2: Suppose the following equation describes the relationship between the average number of classes missed during a semester(missed) and the distance from school ( distance, measured in miles):
import numpy as np
distance = np.array([5.0, 10.0, 20.0])

def missed(distance):
        missed_classes = 3 + 0.2*(distance)
        return missed_classes 

print(missed_classes)

diff_distance = missed_classes[2] - missed_classes[1]
print(diff_distance) # = 2.0



    
    
         
    

