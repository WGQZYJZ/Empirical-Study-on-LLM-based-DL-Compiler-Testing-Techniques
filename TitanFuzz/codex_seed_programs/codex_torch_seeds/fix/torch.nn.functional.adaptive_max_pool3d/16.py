'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_data = Variable(torch.randn(1, 1, 2, 2, 2))
print('input_data:', input_data)
output = torch.nn.functional.adaptive_max_pool3d(input_data, (1, 1, 1))
print('output:', output)