'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
sorted_sequence = torch.arange(10)
values = torch.tensor([2, 3, 5, 7, 8, 9])
torch.searchsorted(sorted_sequence, values, right=False)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
sorted_sequence = torch.arange(10)
values = torch.tensor([2, 3, 5, 7, 8, 9])
torch.searchsorted(sorted_sequence, values, right=True)