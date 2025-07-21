'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli_\ntorch.Tensor.bernoulli_(_input_tensor, p=0.5, *, generator=None)\n'
import torch
import torch
input_tensor = torch.Tensor(3, 5)
input_tensor.uniform_(0, 1)
print('input_tensor:', input_tensor)
output_tensor = torch.Tensor.bernoulli_(input_tensor)
print('output_tensor:', output_tensor)