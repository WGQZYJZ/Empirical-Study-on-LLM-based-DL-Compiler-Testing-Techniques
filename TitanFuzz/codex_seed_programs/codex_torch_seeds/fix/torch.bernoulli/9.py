'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bernoulli\ntorch.bernoulli(input, *, generator=None, out=None)\n'
import torch
input_data = torch.rand(2, 3)
print(input_data)
output_data = torch.bernoulli(input_data)
print(output_data)
output_data = torch.bernoulli(input_data, generator=None, out=None)
print(output_data)