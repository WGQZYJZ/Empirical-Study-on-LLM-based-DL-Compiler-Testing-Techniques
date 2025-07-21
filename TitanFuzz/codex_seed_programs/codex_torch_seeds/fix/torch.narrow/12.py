'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
x = torch.randn(4, 4)
print(x)
print(x.size())
print(x.narrow(0, 0, 2))
print(x.narrow(1, 1, 2))
print(torch.narrow(x, 0, 0, 2))
print(torch.narrow(x, 1, 1, 2))