'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_and\ntorch.bitwise_and(input, other, *, out=None)\n'
import torch
x = torch.tensor([True, False, True, False])
y = torch.tensor([True, True, False, False])
z = torch.bitwise_and(x, y)
print(z)