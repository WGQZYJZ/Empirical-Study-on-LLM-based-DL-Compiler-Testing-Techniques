'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.allclose\ntorch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3)
print(torch.allclose(x, y))
print(torch.allclose(x, y, rtol=1e-05, atol=1e-08))
print(torch.allclose(x, y, rtol=1e-05, atol=1e-08, equal_nan=True))