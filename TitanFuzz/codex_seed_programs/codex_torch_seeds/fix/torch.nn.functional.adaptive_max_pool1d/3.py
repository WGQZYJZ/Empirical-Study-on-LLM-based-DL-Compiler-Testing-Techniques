'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
input_data = Variable(torch.randn(1, 1, 3))
print('Input data: ', input_data)
output = nn.functional.adaptive_max_pool1d(input_data, 1)
print('Output: ', output)