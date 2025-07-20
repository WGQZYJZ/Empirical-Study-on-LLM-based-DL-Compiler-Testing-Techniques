input_data = torch.rand(2, 3)
input_data[0][0] = torch.tensor(float('nan'))
input_data[1][1] = torch.tensor(float('nan'))
output = torch.nanmedian(input_data, dim=1, keepdim=False)