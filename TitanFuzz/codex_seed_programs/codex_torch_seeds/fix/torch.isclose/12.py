'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isclose\ntorch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
input = torch.randn(1, 3)
other = torch.randn(1, 3)
print(torch.isclose(input, other))
print(torch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False))
print(torch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=True))
print(torch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False))