'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
input_data = torch.randn(2, 3, 4)
print('Input data:')
print(input_data)
print('\nOutput data:')
print(torch.moveaxis(input_data, 0, (- 1)))