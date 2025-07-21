'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bernoulli\ntorch.bernoulli(input, *, generator=None, out=None)\n'
import torch
input_data = torch.Tensor([0.2, 0.8])
output = torch.bernoulli(input_data)
print(output)