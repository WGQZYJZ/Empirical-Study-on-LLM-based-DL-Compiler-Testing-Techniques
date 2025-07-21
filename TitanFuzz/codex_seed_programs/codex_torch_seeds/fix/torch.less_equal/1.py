'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less_equal\ntorch.less_equal(input, other, *, out=None)\n'
import torch
input_data = torch.randn(3)
output_data = torch.less_equal(input_data, 0)
print('input_data: ', input_data)
print('output_data: ', output_data)