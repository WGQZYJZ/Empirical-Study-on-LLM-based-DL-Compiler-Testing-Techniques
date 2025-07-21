'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(1, 1, 5))
print('Input data:', input_data)
output = torch.nn.functional.adaptive_max_pool1d(input_data, 2)
print('Output data:', output)
print('Output data shape:', output.shape)
print('Output data:', output)
(output, indices) = torch.nn.functional.adaptive_max_pool1d(input_data, 2, return_indices=True)
print('Output data shape:', output.shape)
print('Output data:', output)
print('Indices shape:', indices.shape)
print('Indices:', indices)