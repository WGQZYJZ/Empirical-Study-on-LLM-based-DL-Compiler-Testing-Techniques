'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input = torch.rand(4, 4)
print(input)
print(torch.flip(input, dims=[1]))
print(torch.flip(input, dims=[0]))
print(torch.flip(input, dims=[0, 1]))