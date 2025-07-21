'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input)
print(torch.special.logsumexp(input, dim=0, keepdim=False))