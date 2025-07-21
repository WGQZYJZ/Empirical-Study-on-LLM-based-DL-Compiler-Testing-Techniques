'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input_data = torch.randint(20, (3, 3), dtype=torch.float)
other_data = torch.randint(10, (3, 3), dtype=torch.float)
output = torch.floor_divide(input_data, other_data)
print('input_data: ', input_data)
print('other_data: ', other_data)
print('output: ', output)