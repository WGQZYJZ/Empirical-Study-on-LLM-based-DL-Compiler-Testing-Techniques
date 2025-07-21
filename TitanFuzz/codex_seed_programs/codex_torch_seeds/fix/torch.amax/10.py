'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
(max_val, max_idx) = torch.amax(input_data, 1)
print(input_data)
print(max_val)
print(max_idx)