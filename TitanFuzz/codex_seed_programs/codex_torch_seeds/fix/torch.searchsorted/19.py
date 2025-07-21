'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
sorted_sequence = torch.arange(10)
values = torch.tensor([3, 4, 1, 8])
result = torch.searchsorted(sorted_sequence, values)
print(result)