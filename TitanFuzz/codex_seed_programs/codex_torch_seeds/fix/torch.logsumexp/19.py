'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logsumexp\ntorch.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input_data = torch.rand(2, 3)
print(input_data)
output_data = torch.logsumexp(input_data, dim=1, keepdim=True)
print(output_data)