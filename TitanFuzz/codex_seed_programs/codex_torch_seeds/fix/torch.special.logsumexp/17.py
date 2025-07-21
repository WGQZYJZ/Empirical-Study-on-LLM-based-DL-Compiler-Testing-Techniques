'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.arange(1, 11, dtype=torch.float32).reshape(2, 5)
print(input_data)
print(torch.special.logsumexp(input_data, dim=1))
print(torch.special.logsumexp(input_data, dim=1, keepdim=True))
print(torch.special.logsumexp(input_data, dim=0))
print(torch.special.logsumexp(input_data, dim=0, keepdim=True))