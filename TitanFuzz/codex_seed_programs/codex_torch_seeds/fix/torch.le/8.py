'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.le(x, 3)
print(y)