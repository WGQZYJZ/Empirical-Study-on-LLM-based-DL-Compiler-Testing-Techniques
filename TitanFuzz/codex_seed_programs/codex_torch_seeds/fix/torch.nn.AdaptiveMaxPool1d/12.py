'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
import torch.nn as nn
input = Variable(torch.randn(1, 1, 10))
pool = nn.AdaptiveMaxPool1d(5)
output = pool(input)
print(output)
print(input)