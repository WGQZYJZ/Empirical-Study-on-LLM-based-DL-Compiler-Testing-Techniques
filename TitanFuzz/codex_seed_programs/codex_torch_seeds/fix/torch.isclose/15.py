'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isclose\ntorch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
x = torch.tensor([1e-06, 1e-07, 1e-08])
y = torch.tensor([1e-06, 1e-08, 1e-07])
print(torch.isclose(x, y, rtol=1e-06, atol=1e-08))
print(torch.isclose(x, y, rtol=1e-06, atol=1e-09))
x = torch.tensor([1e-06, 1e-07, 1e-08])
y = torch.tensor([1e-06, 1e-08, 1e-07])
print(torch.isclose(x, y, rtol=1e-06, atol=1e-08))
print(torch.isclose(x, y, rtol=1e-06, atol=1e-09))