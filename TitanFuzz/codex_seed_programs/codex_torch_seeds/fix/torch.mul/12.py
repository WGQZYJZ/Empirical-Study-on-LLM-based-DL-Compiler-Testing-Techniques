'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
import torch
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[1, 1], [1, 1]])
torch.mul(x, y)
torch.mul(x, y, out=x)