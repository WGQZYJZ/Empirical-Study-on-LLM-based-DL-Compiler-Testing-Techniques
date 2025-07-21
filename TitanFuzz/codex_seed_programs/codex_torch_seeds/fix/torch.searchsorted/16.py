'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
sorted_sequence = torch.arange(10, dtype=torch.float)
values = torch.tensor([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5])
print('Task 3: Call the API torch.searchsorted')
out_int32 = torch.searchsorted(sorted_sequence, values, out_int32=True)
print('out_int32 = ', out_int32)
out_int64 = torch.searchsorted(sorted_sequence, values, out_int32=False)
print('out_int64 = ', out_int64)
out_right = torch.searchsorted(sorted_sequence, values, right=True)
print('out_right = ', out_right)