from itertools import permutations

def solution(k, dungeons):
    answer = 0   
    
    fullPerms = list(permutations(dungeons))    
    
    for perm in fullPerms:
        tempK = k 
        count = 0          
        
        for required, cost in perm:            
            if tempK >= required:
                tempK -= cost  
                count += 1             
        
        answer = max(answer, count)
    
    return answer

ex1 = [80, [[80,20],[50,40],[30,10]]]
print(solution(ex1[0], ex1[1]))