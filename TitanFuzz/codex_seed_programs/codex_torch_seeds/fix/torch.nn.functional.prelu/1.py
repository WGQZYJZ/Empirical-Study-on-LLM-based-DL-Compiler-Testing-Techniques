'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight)\n'
import torch
import torch.nn.functional as F
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 3, 3))
weight = Variable(torch.randn(1))
output = F.prelu(input, weight)
print('input:', input)
print('weight:', weight)
print('output:', output)