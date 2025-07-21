'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isclose\ntorch.isclose(input, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
diff = (x - y)
result = torch.isclose(diff, torch.zeros(5, 3))
print(result)