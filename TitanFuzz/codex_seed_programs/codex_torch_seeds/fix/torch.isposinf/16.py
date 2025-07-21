'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
import torch
input = torch.rand(1, 3)
print(input)
print(torch.isposinf(input))
print(torch.isposinf(torch.tensor([float('inf')])))
print(torch.isposinf(torch.tensor([float('-inf')])))
print(torch.isposinf(torch.tensor([float('nan')])))
print(torch.isposinf(torch.tensor([1.0])))