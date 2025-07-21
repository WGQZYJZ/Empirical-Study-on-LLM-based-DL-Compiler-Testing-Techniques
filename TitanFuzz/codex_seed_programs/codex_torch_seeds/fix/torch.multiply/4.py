'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multiply\ntorch.multiply(input, other, *, out=None)\n'
import torch
a = torch.tensor([2, 4, 6])
b = torch.tensor([1, 2, 3])
print(torch.multiply(a, b))