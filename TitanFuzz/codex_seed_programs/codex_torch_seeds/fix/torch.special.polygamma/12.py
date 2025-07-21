'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
data = torch.rand(10, dtype=torch.float64)
result = torch.special.polygamma(1, data)
print(result)