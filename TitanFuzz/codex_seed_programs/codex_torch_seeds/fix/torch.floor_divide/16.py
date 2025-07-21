'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input_data = torch.randint(10, (5, 3), dtype=torch.float)
print('Input data:\n', input_data)
output_data = torch.floor_divide(input_data, 2)
print('Output data:\n', output_data)
'\ntorch.fmod(input, divisor, *, out=None)\n'
input_data = torch.randint(10, (5, 3), dtype=torch.float)
print('Input data:\n', input_data)
output_data = torch.fmod(input_data, 2)
print('Output data:\n', output_data)
'\ntorch.fmod(input, divisor, *, out=None)\n'
input_data = torch.randint(10, (5, 3), dtype=torch.float)
print('Input data:\n', input_data)