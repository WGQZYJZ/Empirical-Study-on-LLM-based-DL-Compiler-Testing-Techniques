'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.glu\ntorch.nn.functional.glu(input, dim=-1)\n'
import torch
input_data = torch.randn(2, 3, 4)
print('Input data: \n', input_data, '\n')
output_data = torch.nn.functional.glu(input_data, dim=(- 1))
print('Output data: \n', output_data, '\n')