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

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        torch.manual_seed(1)
        self.conv = torch.nn.Conv2d(3, 3, 3)
        torch.manual_seed(1)
        self.bn = torch.nn.BatchNorm2d(1)
        self.bn.weight.data = torch.ones(1)
        self.bn.bias.data = torch.zeros(1)

    def forward(self, x2):
        v1 = self.bn(x2)
        v2 = self.conv(v1)
        v2 = self.bn(v2)
        return v2



func = Model().to('cpu')

x2 = 1

test_inputs = [x2]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'dim'

jit:
AttributeError: 'int' object has no attribute 'dim'

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 160, in forward
    self._check_input_dim(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 451, in _check_input_dim
    if input.dim() != 4:


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''