'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.subtract\ntorch.subtract(input, other, *, alpha=1, out=None)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
print(torch.subtract(a, b))
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
print((a - b))