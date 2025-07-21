'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_data = Variable(torch.randn(1, 1, 10, 10))
output = torch.nn.functional.adaptive_max_pool2d(input_data, (5, 5))
print(output)