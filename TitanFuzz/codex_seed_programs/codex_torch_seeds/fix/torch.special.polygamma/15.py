'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
import torch
input = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
output = torch.special.polygamma(1, input)
print(output)
output = torch.special.polygamma(3, input)
print(output)