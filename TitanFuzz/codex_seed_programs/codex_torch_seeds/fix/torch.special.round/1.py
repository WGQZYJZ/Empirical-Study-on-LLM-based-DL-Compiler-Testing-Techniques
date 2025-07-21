'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.round\ntorch.special.round(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0])
output_data = torch.special.round(input_data)
print('Input data: ', input_data)
print('Output data: ', output_data)