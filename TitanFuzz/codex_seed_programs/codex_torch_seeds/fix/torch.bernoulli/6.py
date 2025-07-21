'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bernoulli\ntorch.bernoulli(input, *, generator=None, out=None)\n'
import torch
input_data = torch.rand(3, 3)
print('Input Data: ', input_data)
output_data = torch.bernoulli(input_data)
print('Output Data: ', output_data)