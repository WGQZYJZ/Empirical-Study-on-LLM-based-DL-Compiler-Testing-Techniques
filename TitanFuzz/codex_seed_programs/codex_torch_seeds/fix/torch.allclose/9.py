'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.allclose\ntorch.allclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
a = torch.tensor([1.0, 2.0, 3.0, 4.0])
b = torch.tensor([1.0, 2.0, 3.0, 4.0])
print(torch.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False))