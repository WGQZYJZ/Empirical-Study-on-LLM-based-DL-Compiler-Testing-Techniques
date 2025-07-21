'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.pow(x, 2)
print(y)