'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input_data = torch.rand(2, 3)
input_data[0][0] = torch.tensor(float('nan'))
input_data[1][1] = torch.tensor(float('nan'))
print('Input Data: ', input_data)
output = torch.nanmedian(input_data, dim=1, keepdim=False)
print('Output: ', output)