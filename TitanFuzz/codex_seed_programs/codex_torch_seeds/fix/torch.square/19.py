'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print(x)
y = torch.square(x)
print(y)
'\ntorch.add(input, other, *, out=None)\n'
x1 = torch.randn(2, 3)
x2 = torch.randn(2, 3)
y1 = torch.add(x1, x2)
print(y1)
y2 = torch.add(x1, 10)
print(y2)
y3 = torch.add(10, x1)
print(y3)
y4 = torch.add(x1, x2, alpha=0.5)
print(y4)