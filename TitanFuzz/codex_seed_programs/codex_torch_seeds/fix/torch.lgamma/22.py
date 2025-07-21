'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
input = torch.Tensor([1, 2, 3, 4, 5])
print(torch.lgamma(input))