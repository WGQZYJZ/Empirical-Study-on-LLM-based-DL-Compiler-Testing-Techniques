'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isclose\ntorch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
x = torch.rand(10)
y = torch.rand(10)
print(torch.isclose(x, y))
print(torch.isclose(x, y, atol=0.5))
print(torch.isclose(x, y, rtol=0.5))