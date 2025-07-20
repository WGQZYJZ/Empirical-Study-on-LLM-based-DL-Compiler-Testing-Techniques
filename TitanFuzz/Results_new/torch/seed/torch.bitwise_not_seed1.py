input_data = torch.randint(0, 2, (2, 3), dtype=torch.uint8)
output_data = torch.bitwise_not(input_data)