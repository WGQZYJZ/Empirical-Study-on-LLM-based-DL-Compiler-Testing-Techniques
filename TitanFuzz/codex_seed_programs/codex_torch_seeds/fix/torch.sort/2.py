'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 5)
(sorted_input, sorted_index) = torch.sort(input, dim=0)
print('sorted_input: ', sorted_input)
print('sorted_index: ', sorted_index)