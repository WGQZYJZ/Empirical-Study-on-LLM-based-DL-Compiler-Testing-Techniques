'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
import torch
input = torch.randn(4, 4)
print(input)
print(torch.narrow(input, 0, 0, 2))
print(torch.narrow(input, 1, 1, 3))