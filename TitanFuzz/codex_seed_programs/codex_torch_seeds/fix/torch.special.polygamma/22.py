'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
import torch.nn.functional as F
import torch
input = torch.rand(3, 4, 5, dtype=torch.float64)
output = torch.special.polygamma(3, input)
print(output)
output = torch.special.polygamma(3, input, out=torch.empty(3, 4, 5, dtype=torch.float64))
print(output)