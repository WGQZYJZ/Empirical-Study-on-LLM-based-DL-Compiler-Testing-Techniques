'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), (- 2), 3, 4, 5])
print('input_data: ', input_data)
output_data = torch.abs(input_data)
print('output_data: ', output_data)