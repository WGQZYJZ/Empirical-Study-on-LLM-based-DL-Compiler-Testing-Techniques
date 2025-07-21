'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
x = torch.randn(3, 4, 5)
print(x)
y = torch.moveaxis(x, 0, 1)
print(y)
y = torch.moveaxis(x, 0, (- 1))
print(y)
y = torch.moveaxis(x, (- 1), 0)
print(y)