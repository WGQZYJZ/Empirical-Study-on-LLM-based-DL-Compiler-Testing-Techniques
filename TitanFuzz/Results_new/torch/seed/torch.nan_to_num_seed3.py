input = torch.randn(4, 4)
input[(0, 0)] = float('nan')
input[(1, 1)] = float('inf')
input[(2, 2)] = float('-inf')
output = torch.nan_to_num(input)