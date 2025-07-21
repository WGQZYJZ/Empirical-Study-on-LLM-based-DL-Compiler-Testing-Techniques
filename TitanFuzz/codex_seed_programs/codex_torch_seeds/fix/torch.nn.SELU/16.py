'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
x = Variable(torch.randn(2, 3))
selu = nn.SELU(inplace=False)
print(selu(x))