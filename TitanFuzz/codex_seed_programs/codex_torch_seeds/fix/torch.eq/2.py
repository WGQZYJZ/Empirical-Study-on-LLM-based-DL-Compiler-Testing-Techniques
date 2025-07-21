'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3])
y = torch.tensor([1, 2, 3])
z = torch.tensor([1, 2, 4])
print(torch.eq(x, y))
print(torch.eq(x, z))