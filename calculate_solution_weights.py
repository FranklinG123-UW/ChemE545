def calculate_solution_weights(molecular_weights, solutions_needed): 
    new_list = []
    for i in range(len(solutions_needed)): #loops through all strings in sol_needed list
            #finds index of the dash in the string
            dash_index = solutions_needed[i].index('-') 
            #finds index of the end of the concentration value    
            end_index = len(solutions_needed[i])-1 
            #gives the value of the concentration as a float
            concentration = float(solutions_needed[i][dash_index+1:end_index])
            #name of chemical at index i as a string
            chemical_name = solutions_needed[i][0:dash_index]
    
            #begin the concatenation process, checking to see if chem exists in dictionary
            if chemical_name in molecular_weights: # if soln at index exists in MW dictionary
                #our wt in grams to be added to end of name
                weight = molecular_weights[chemical_name] * concentration
                #append this weight to the end of solution_needed at index i, formatted to end in grams
                new_entry = solutions_needed[i] + "-" + str(weight) +"g"
                new_list.append(new_entry)
            else: #if soln at index is not in our mol wt dictionary
                new_list.append("unknown")
            
    return new_list #returns our list, appended with the edited strings and unknown values

calculate_solution_weights(molecular_weights, solutions_needed
