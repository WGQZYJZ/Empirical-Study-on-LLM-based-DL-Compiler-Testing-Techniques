'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
input = Variable(torch.randn(1, 1, 4))
pooling = nn.LPPool1d(norm_type=2, kernel_size=2, stride=2)
output = pooling(input)
print('Input:')
print(input)
print('Output:')
print(output)
'\nTask 5: import PyTorch\nTask 6: Generate input data\nTask 7: Call the API torch.nn.LPPool2d\ntorch.nn.LPPool2d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
input = Variable(torch.randn(1, 1, 4, 4))