'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
import torch
data = Variable(torch.randn(1, 1, 8, 8))
result = F.adaptive_max_pool2d(data, (3, 3))
print(result.data)
print(result.shape)