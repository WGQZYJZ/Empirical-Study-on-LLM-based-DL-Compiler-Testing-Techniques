'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argsort\ntorch.argsort(input, dim=-1, descending=False)\n'
import torch
input = torch.randn(3, 4)
print('Input data: \n', input)
sort_index = torch.argsort(input, dim=(- 1), descending=False)
print('Sort index: \n', sort_index)
sort_data = torch.gather(input, dim=(- 1), index=sort_index)
print('Sort data: \n', sort_data)