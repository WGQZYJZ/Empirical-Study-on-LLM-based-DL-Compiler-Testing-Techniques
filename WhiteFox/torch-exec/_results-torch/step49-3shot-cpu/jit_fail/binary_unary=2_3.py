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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.fc_1 = nn.Linear(3, 3)
        self.maxpool = nn.MaxPool2d(4, stride=4)
        self.fc_2 = nn.Linear(3, 1)

    def forward(self, x):
        x = self.fc_1(x)
        x = self.maxpool(x)
        x = self.fc_2(x)
        x = F.flatten(x)
        return x



func = Model().to('cpu')


x1 = torch.randn(1, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-empty 3D or 4D (batch mode) tensor expected for input

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7161b6de0ee0>(*(FakeTensor(..., size=(1, 3)), 4, 4, 0, 1), **{'ceil_mode': False, 'return_indices': False}):
Dimension out of range (expected to be in range of [-2, 1], but got -3)

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''