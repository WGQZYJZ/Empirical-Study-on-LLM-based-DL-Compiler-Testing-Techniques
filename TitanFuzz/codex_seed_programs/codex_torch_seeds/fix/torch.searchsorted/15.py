'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
sorted_sequence = torch.tensor([1, 3, 4, 5, 6, 8, 9])
values = torch.tensor([1, 4, 6, 7, 10])
result = torch.searchsorted(sorted_sequence, values, right=True)
print('sorted_sequence: ', sorted_sequence)
print('values: ', values)
print('result: ', result)