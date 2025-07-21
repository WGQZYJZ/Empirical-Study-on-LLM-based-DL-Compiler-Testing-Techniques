'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logsumexp\ntorch.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('input_data: ', input_data)
print('dim=0: ', torch.logsumexp(input_data, dim=0))
print('dim=1: ', torch.logsumexp(input_data, dim=1))
print('dim=1, keepdim=True: ', torch.logsumexp(input_data, dim=1, keepdim=True))