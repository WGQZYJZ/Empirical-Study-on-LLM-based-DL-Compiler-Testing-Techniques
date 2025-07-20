input_data = torch.arange(0, 24).view(2, 3, 4)
output_data = torch.swapaxes(input_data, 1, 2)