'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
sorted_sequence = torch.randn(10)
values = torch.randn(5)
result = torch.searchsorted(sorted_sequence, values)
print(result)