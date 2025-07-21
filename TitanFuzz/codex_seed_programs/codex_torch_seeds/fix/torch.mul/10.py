'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
import torch
input_data = torch.rand(2, 3)
other_data = torch.rand(2, 3)
result = torch.mul(input_data, other_data)
print('input_data: {}'.format(input_data))
print('other_data: {}'.format(other_data))
print('result: {}'.format(result))
output_data = torch.zeros(2, 3)
result = torch.mul(input_data, other_data, out=output_data)
print('input_data: {}'.format(input_data))
print('other_data: {}'.format(other_data))
print('output_data: {}'.format(output_data))
print('result: {}'.format(result))