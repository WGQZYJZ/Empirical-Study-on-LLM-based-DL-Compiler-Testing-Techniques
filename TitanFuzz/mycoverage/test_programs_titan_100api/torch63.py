import torch
input = torch.randn(4, 4)
input[(2, 3)] = float('NaN')
input[(3, 2)] = float('NaN')
nansum = torch.nansum(input)