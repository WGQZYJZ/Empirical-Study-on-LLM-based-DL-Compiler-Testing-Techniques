'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch
from torch.autograd import Variable
import torch.nn as nn
input = Variable(torch.randn(1, 3, 5, 5))
pool = nn.AdaptiveAvgPool2d(output_size=(3, 3))
output = pool(input)
print('input: ', input)
print('output: ', output)