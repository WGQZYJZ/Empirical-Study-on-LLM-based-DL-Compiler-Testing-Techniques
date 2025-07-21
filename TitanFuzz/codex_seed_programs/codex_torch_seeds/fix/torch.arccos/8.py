'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccos\ntorch.arccos(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.0, 0.5, 1.0])
output = torch.arccos(input_data)
print('Input data: ', input_data)
print('Output: ', output)