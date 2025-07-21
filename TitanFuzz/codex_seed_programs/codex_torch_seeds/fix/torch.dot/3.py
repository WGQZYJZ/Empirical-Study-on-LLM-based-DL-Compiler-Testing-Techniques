'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dot\ntorch.dot(input, other, *, out=None)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
print(torch.dot(a, b))