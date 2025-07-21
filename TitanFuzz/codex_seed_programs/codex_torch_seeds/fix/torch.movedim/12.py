'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.movedim\ntorch.movedim(input, source, destination)\n'
import torch
data_size = 10
data_input = torch.randn(data_size, 3, 5)
print('Input data = ', data_input)
print('Input data size = ', data_input.size())
print('Input data shape = ', data_input.shape)
print('\nMove the dimension from 2 to 0')
data_output = torch.movedim(data_input, 2, 0)
print('Output data = ', data_output)
print('Output data size = ', data_output.size())
print('Output data shape = ', data_output.shape)