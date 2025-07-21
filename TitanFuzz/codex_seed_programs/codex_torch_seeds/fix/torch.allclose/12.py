'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.allclose\ntorch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
a = torch.randn(2, 3)
b = torch.randn(2, 3)
print(a)
print(b)
print(torch.allclose(a, b))
print(torch.allclose(a, b, rtol=1e-05, atol=1e-08))
print(torch.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=True))