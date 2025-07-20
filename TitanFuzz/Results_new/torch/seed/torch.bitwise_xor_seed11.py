input_data = torch.randint(0, 2, (10,))
other_data = torch.randint(0, 2, (10,))
output_data = torch.bitwise_xor(input_data, other_data)