'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isclose\ntorch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
x = torch.tensor([0.0001, 1e-05, 1e-10])
y = torch.tensor([0.0001, 1e-05, 1e-10])
out = torch.isclose(x, y, rtol=1e-05, atol=1e-08, equal_nan=False)
print(out)