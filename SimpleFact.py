facts = [
"john_is_cold.",
"raining.",
"john_Forgot_His_Raincoat.",  
"fred_lost_his_car_keys.",    
"peter_footballer."
]
def verify_fact(fact):
    fact = fact.rstrip(".")
    if fact == "john_Forgot_His_Raincoat":
      return True
    elif fact == "raining":
        return True
    elif fact == "foggy":
        return True
    elif fact == "Cloudy":
        return False  
    else:
        return False

for fact in facts:
    if verify_fact(fact):
        print(f"{fact} - Yes")
    else:
        print(f"{fact} - No")
