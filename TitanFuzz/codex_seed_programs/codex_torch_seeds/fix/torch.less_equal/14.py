'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less_equal\ntorch.less_equal(input, other, *, out=None)\n'
import torch
input_data = torch.rand(4, 4)
print('Input data: ', input_data)
output = torch.less_equal(input_data, 0.5)
print('Output data: ', output)