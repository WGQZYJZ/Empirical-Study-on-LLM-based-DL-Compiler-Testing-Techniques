'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli_\ntorch.Tensor.bernoulli_(_input_tensor, p=0.5, *, generator=None)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data: {}'.format(input_data))
output = torch.Tensor.bernoulli_(input_data)
print('Output data: {}'.format(output))