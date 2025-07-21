'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
x = torch.rand(5, 3)
print(x)
print(torch.narrow(x, 0, 0, 2))
print(torch.narrow(x, 1, 1, 2))