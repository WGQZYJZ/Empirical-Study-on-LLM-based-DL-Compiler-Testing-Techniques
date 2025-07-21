'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
input = torch.rand(3, 3)
print('Input:', input)
narrowed = torch.narrow(input, 1, 1, 2)
print('Narrowed:', narrowed)