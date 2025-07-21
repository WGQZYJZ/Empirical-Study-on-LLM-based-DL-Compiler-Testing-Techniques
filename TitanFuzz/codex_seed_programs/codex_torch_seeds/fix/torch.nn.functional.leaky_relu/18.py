'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
from torch.autograd import Variable
from torch.nn import functional as F
input = Variable(torch.randn(1, 1, 3, 3))
print('input:', input)
output = F.leaky_relu(input, negative_slope=0.01, inplace=False)
print('output:', output)