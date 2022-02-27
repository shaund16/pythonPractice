def kooka_counter(laughing):
    return 0 if laughing == '' else laughing.count('Hah') + laughing.count('haH') + 1
    
print(kooka_counter("hahahahaha"))
print(kooka_counter("hahahahahaHaHaHa"))
print(kooka_counter("HaHaHahahaHaHa"))