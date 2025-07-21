'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch
x = Variable(torch.randn(1, 1, 6))
print('Input data: ', x)
pool1d = nn.AdaptiveMaxPool1d(4)
print('AdaptiveMaxPool1d: ', pool1d(x))