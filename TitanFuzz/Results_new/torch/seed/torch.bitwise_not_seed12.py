input_data = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
output = torch.bitwise_not(input_data)