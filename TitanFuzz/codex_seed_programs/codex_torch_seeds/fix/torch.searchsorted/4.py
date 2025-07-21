'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
sorted_sequence = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
values = torch.tensor([2, 4, 6, 8, 10])
out = torch.searchsorted(sorted_sequence, values, right=False)
print(out)