'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
input = torch.randn(3, 4)
print(input)
print(torch.narrow(input, 0, 0, 2))
print(torch.narrow(input, 1, 1, 2))
print(torch.narrow(input, 1, 0, 2))