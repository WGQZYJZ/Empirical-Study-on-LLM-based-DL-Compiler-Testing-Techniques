'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isclose\ntorch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
a = torch.rand(100, 100)
b = torch.rand(100, 100)
c = torch.isclose(a, b)
print(c)