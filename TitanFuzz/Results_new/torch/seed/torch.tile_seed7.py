input_data = torch.arange(9)
input_data = input_data.reshape(3, 3)
output_data = torch.tile(input_data, (2, 3))