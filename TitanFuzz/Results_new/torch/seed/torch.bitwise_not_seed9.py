input_data = torch.randint(0, 2, size=(2, 3), dtype=torch.int8)
output = torch.bitwise_not(input_data)