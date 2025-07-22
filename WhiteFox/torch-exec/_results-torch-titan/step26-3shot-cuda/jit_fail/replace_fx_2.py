import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.net = nn.RNN(32, 16, 2, batch_first=True, dropout=0.0, bidirectional=True)

    def forward(self, x):
        x4 = self.net(x)
        x5 = torch.rand_like(x4, requires_grad=True)
        return x5




func = Net().to('cuda')



x = torch.randn(10, 13, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
rand_like(): argument 'input' (position 1) must be Tensor, not tuple

jit:
rand_like(): argument 'input' (position 1) must be Tensor, not tuple
'''