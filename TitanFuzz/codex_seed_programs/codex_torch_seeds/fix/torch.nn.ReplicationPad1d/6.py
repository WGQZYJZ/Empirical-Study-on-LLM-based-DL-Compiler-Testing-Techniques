'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch
from torch.autograd import Variable
input = Variable(torch.ones(1, 1, 3))
pad = nn.ReplicationPad1d(2)
output = pad(input)
print('input: ', input)
print('output: ', output)