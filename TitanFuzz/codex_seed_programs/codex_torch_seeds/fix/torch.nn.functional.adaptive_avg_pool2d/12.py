'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
from torch.nn.functional import adaptive_avg_pool2d
input_data = torch.randn(1, 1, 4, 4)
print('Input Data: ', input_data)
output_size = (2, 2)
output = adaptive_avg_pool2d(input_data, output_size)
print('Output: ', output)