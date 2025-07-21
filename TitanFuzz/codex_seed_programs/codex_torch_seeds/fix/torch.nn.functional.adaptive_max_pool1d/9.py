'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 10))
print('Input data: ', input)
output = torch.nn.functional.adaptive_max_pool1d(input, 3)
print('Output data: ', output)
print('Output shape: ', output.shape)