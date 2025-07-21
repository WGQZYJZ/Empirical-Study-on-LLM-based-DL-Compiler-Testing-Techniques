'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(10, 5)
print(torch.special.logsumexp(input_data, dim=0))