'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
y = torch.tensor([1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
result = torch.eq(x, y)
print(result)