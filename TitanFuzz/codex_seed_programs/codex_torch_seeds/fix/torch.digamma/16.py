'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
input_data = torch.randn(10)
print('Input data is: ', input_data)
digamma_data = torch.digamma(input_data)
print('Digamma data is: ', digamma_data)