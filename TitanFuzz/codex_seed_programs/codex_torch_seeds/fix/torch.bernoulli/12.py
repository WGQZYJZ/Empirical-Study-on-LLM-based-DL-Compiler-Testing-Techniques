'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bernoulli\ntorch.bernoulli(input, *, generator=None, out=None)\n'
import torch
input = torch.Tensor([0.2, 0.3, 0.8, 0.6])
output = torch.bernoulli(input)
print(output)
output = torch.bernoulli(torch.Tensor([0.2]))
print(output)
input = torch.Tensor([0.2, 0.3, 0.8, 0.6])
output = torch.bernoulli(input)
print(output)
input = torch.Tensor([0.2, 0.3, 0.8, 0.6])
output = torch.bernoulli(input)
print(output)