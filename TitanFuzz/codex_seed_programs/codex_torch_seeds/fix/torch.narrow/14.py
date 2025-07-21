'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
import torch
x = torch.rand(3, 10)
print(torch.narrow(x, 1, 0, 5))
print(torch.narrow(x, 1, 5, 5))