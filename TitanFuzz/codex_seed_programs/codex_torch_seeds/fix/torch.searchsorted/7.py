'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
sorted_sequence = torch.arange(0, 10, 2)
values = torch.tensor([1, 2, 4, 5, 6, 8, 9])
result = torch.searchsorted(sorted_sequence, values)
print(result)
result = torch.searchsorted(sorted_sequence, values, right=True)
print(result)