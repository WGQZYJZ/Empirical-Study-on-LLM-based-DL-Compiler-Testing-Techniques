'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('input_data:\n', input_data)
print('input_data.size():\n', input_data.size())
cumsum_output = torch.cumsum(input_data, dim=1)
print('cumsum_output:\n', cumsum_output)
print('cumsum_output.size():\n', cumsum_output.size())
cumsum_output = torch.cumsum(input_data, dim=0)
print('cumsum_output:\n', cumsum_output)
print('cumsum_output.size():\n', cumsum_output.size())