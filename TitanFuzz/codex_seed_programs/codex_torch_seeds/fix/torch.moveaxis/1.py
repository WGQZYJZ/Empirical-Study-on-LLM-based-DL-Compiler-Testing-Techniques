'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input_data = torch.randn(2, 3, 4)
print('Input data: \n', input_data)
output_data = torch.moveaxis(input_data, 2, 0)
print('\nOutput data: \n', output_data)
output_data = torch.moveaxis(input_data, 1, 2)
print('\nOutput data: \n', output_data)