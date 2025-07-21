'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input_data = torch.tensor([3.1, (- 3.1), 4.8, (- 4.8)])
print('Input data: ', input_data)
output = torch.ceil(input_data)
print('Output data: ', output)