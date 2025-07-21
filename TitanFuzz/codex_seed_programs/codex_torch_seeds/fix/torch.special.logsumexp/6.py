'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print()
print('Task 2: Generate input data')
input_data = torch.rand(4, 4)
print('input_data: ', input_data)
print()
print('Task 3: Call the API torch.special.logsumexp')
print('torch.special.logsumexp(input_data, dim=1, keepdim=False): ', torch.special.logsumexp(input_data, dim=1, keepdim=False))
print('torch.special.logsumexp(input_data, dim=1, keepdim=True): ', torch.special.logsumexp(input_data, dim=1, keepdim=True))