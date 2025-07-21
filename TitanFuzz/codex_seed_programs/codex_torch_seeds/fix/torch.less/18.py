'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
other_data = torch.randn(2, 3)
print('input_data: \n{}\n'.format(input_data))
print('other_data: \n{}\n'.format(other_data))
output_data = torch.less(input_data, other_data)
print('output_data: \n{}\n'.format(output_data))