'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logsumexp\ntorch.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(2, 4)
print('Input Data: ', input_data)
output_data = torch.logsumexp(input_data, dim=1)
print('Output Data: ', output_data)