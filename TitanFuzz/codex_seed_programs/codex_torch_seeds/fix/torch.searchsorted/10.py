'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
sorted_sequence = torch.arange(1, 6)
print(sorted_sequence)
values = torch.tensor([1, 3, 5, 7])
print(values)
print(torch.searchsorted(sorted_sequence, values))
print(torch.searchsorted(sorted_sequence, values, right=True))