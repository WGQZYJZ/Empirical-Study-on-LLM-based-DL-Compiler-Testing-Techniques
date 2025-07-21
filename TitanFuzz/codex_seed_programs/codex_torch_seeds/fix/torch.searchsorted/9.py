'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
sorted_sequence = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9])
values = torch.tensor([3, 2, 4, 5, 1, 8, 7, 6, 9])
torch.searchsorted(sorted_sequence, values, out_int32=False, right=False, out=None)