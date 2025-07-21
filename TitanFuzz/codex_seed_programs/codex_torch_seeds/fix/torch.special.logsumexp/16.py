'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logsumexp\ntorch.special.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(1, 2)
print('input_data:', input_data)
output_data = torch.special.logsumexp(input_data, dim=1, keepdim=False)
print('output_data:', output_data)