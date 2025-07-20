input = torch.tensor([float('NaN'), float('NaN'), float('Inf'), float('-Inf')])
output = torch.nan_to_num(input)