'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
import torch
x = torch.tensor([1, 3, 5, 7, 9])
y = torch.tensor([2, 4, 6, 8, 10])
print(torch.searchsorted(x, y))