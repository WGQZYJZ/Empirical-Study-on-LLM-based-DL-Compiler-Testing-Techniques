'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.poisson\ntorch.poisson(input, generator=None)\n'
import torch
import torch
input = torch.rand(100)
output = torch.poisson(input)
print(output)