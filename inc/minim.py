def my_generator():
    yield [2, 26, 0.0026330491234133465]

# Create an instance of the generator
gen = my_generator()

# Iterate over the generator and print each value
for value in gen:
    print(value)
