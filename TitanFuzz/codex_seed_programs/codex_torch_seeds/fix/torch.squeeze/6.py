'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
x = torch.zeros(2, 1, 2, 1, 2)
print(x)
print(torch.squeeze(x))
print(torch.squeeze(x, 0))
print(torch.squeeze(x, 1))
print(torch.squeeze(x, 2))
print(torch.squeeze(x, 3))
print(torch.squeeze(x, 4))