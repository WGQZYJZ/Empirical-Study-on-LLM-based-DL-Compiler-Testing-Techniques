'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.allclose\ntorch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.allclose(a, b)
print(c)