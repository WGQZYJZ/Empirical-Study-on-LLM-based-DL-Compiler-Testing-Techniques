'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.searchsorted\ntorch.searchsorted(sorted_sequence, values, *, out_int32=False, right=False, out=None)\n'
import torch
sorted_sequence = torch.arange(10, dtype=torch.float)
values = torch.tensor([0.1, 1.2, 5.4, 9.1])
output = torch.searchsorted(sorted_sequence, values)
print(output)
output = torch.searchsorted(sorted_sequence, values, right=True)
print(output)