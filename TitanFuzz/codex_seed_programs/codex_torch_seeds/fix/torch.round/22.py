'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.Tensor([(- 1.5), (- 1.1), (- 0.5), 0.0, 0.5, 1.1, 1.5])
output_data = torch.round(input_data)
print('The input data: \n', input_data)
print('\nThe output data: \n', output_data)