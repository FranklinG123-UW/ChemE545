def extract_parameter(unit_name, parameter_name, index):
    try:
        # Code that may raise an exception
        unit = unit_operations_data[unit_name] # accesses the unit
        parameter = unit[parameter_name] # given a unit, accesses a parameter
        value = parameter[index] # given a parameter within a unit, gives the value of the index 
        
        #must be returned in format {unit_name}_{parameter_name}_{value}
        result = f"{unit_name}_{parameter_name}_{value}"
        return result
    except:
        # if exception occurs, run the next block
        print("Invalid Input")
        
extract_parameter("distillation_column","temperature",1)
