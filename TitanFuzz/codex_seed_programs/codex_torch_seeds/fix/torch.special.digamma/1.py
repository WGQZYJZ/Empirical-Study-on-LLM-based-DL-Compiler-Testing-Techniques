'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
input_data = torch.Tensor([1, 2, 3])
output = torch.special.digamma(input_data)
print('input_data: ', input_data)
print('output: ', output)