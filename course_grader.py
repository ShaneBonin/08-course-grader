def course_grader(param):
     total = 0
    for score in param:
        if score < 50:
            return "fail"
         
        total = total + score
    average = total / len(param)
    
    if average < 70:
        return "fail"
        
    
    
    return "pass"
