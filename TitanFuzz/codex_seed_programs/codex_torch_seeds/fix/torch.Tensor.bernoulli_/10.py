'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli_\ntorch.Tensor.bernoulli_(_input_tensor, p=0.5, *, generator=None)\n'
import torch
input_tensor = torch.rand(5, 3)
print(input_tensor)
output_tensor = torch.Tensor.bernoulli_(input_tensor, p=0.5, generator=None)
print(output_tensor)