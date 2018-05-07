def make_average():
    series = []
    
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    
    return averager

avg = make_average()

print(avg(10))
print(avg(11))
print(avg(12))