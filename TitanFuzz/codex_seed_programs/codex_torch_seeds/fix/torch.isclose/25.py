'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isclose\ntorch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
input = torch.tensor([1.0, 2.0, 3.0, 4.0])
other = torch.tensor([1.0, 2.0, 3.0, 4.0])
result = torch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)
print(result)