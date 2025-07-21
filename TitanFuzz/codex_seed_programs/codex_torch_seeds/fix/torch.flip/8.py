'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input = torch.rand(2, 3, 3)
print(input)
print(input.size())
output = torch.flip(input, dims=[1])
print(output)