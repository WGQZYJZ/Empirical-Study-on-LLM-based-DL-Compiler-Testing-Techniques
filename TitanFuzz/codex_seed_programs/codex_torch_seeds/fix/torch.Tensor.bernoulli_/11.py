'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli_\ntorch.Tensor.bernoulli_(_input_tensor, p=0.5, *, generator=None)\n'
import torch
input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor.bernoulli_(input_tensor, p=0.5, generator=None)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)