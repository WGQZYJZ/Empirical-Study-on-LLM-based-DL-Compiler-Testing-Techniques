'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bernoulli\ntorch.bernoulli(input, *, generator=None, out=None)\n'
import torch
input = torch.rand(2, 3)
print('Input data: ', input)
binary_data = torch.bernoulli(input)
print('Binary data: ', binary_data)
probability = torch.tensor([0.2, 0.5, 0.7])
binary_data = torch.bernoulli(probability)
print('Binary data with given probability: ', binary_data)