input_data = torch.arange(0, 24).view(2, 3, 4)
output = torch.permute(input_data, (1, 0, 2))