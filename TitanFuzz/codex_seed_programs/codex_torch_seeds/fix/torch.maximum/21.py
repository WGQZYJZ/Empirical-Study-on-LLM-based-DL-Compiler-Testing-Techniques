'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.maximum\ntorch.maximum(input, other, *, out=None)\n'
import torch
input_data = torch.rand(3, 4)
print('Input data:\n{}'.format(input_data))
other_data = torch.ones(3, 4)
print('Other data:\n{}'.format(other_data))
output_data = torch.maximum(input_data, other_data)
print('Output data:\n{}'.format(output_data))