'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
input = Variable(torch.Tensor(1, 1, 4, 4).uniform_((- 1), 1))
print(input)
adaptive_max_pool = nn.AdaptiveMaxPool2d(output_size=(2, 2))
output = adaptive_max_pool(input)
print(output)