'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logsumexp\ntorch.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('input_data: ', input_data)
logsumexp_output = torch.logsumexp(input_data, dim=1)
print('logsumexp_output: ', logsumexp_output)