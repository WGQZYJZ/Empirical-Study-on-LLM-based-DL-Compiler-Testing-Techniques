'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
input = Variable(torch.randn(5, 3))
print('Input: ', input)
dropout = nn.AlphaDropout(p=0.5, inplace=False)
output = dropout(input)
print('Output: ', output)