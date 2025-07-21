'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isclose\ntorch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
data1 = torch.randn(5, 5)
data2 = torch.randn(5, 5)
print(torch.isclose(data1, data2, atol=0.1))