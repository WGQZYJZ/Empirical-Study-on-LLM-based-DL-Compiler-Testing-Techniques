'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.BoolStorage\ntorch.BoolStorage(*args, **kwargs)\n'
import torch
input_data = [1, 0, 0, 1, 1, 0, 1, 1]
output = torch.BoolStorage(input_data)
print('Type of the output: {}'.format(type(output)))
print('Input data: {}'.format(input_data))
print('Output: {}'.format(output))