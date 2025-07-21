'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 3, 3))
import torch.nn as nn
input = Variable(torch.randn(1, 1, 3, 3))
selu = nn.SELU(inplace=False)
output = selu(input)
print(output)