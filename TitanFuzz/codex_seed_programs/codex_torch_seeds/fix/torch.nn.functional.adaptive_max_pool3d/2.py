'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = Variable(torch.randn(1, 1, 5, 5, 5))
print('Task 3: Call the API torch.nn.functional.adaptive_max_pool3d')
print(F.adaptive_max_pool3d(input, (3, 3, 3)))