'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('input_data: ', input_data)
(mode_value, mode_idx) = torch.mode(input_data, dim=(- 1), keepdim=False, out=None)
print('mode_value: ', mode_value)
print('mode_idx: ', mode_idx)