'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trapezoid\ntorch.trapezoid(y, x=None, *, dx=None, dim=- 1)\n'
import torch
y = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.trapezoid(y)
print('output = ', output)