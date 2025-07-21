'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
sorted_sequence = torch.tensor([1, 3, 4, 7, 8, 9, 10], dtype=torch.float)
values = torch.tensor([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dtype=torch.float)
out = torch.searchsorted(sorted_sequence, values, out_int32=False, right=False, out=None)
print(out)