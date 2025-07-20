input_data = torch.arange(0, 12)
output = torch.chunk(input_data, 3, dim=0)