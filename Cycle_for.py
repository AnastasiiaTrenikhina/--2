list_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for i in list_:
    print('Я езжу на автомобиле марки', i)
    cars_count = 0
    for item in list_:
        cars_count += 10
        print(f'Я езжу на автомобиле марки, {cars_count}')

