'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.add\ntorch.add(input, other, *, alpha=1, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([1, 1, 1, 1, 1])
print(x)
print(y)
print(torch.add(x, y))