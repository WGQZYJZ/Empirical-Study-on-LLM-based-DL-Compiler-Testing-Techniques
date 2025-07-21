'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.var_mean\ntorch.var_mean(input, dim, unbiased, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print('Input data: \n', input)
print('Variance and mean with dim = 0: \n', torch.var_mean(input, 0))
print('Variance and mean with dim = 1: \n', torch.var_mean(input, 1))
print('Variance and mean with unbiased = True, dim = 0: \n', torch.var_mean(input, 0, True))
print('Variance and mean with unbiased = False, dim = 0: \n', torch.var_mean(input, 0, False))
print('Variance and mean with unbiased = True, dim = 1: \n', torch.var_mean(input, 1, True))