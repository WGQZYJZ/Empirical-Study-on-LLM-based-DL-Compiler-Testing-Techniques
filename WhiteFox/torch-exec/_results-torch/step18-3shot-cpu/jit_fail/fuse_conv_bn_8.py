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
        self.conv1 = torch.nn.Conv2d(3, 3, 3)
        self.conv2 = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3)
        self.relu = torch.nn.ReLU()
        self.cat = torch.nn.quantized.FloatFunctional()

    def forward(self, x1):
        s = self.conv1(x1)
        t = self.conv2(s)
        y = self.bn(t)
        z = self.cat.cat([x1, y], dim=1)
        z = self.relu(z)
        return s



func = Model().to('cpu')


x1 = torch.randn(1, 3, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 6 but got size 2 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7af6bf996ec0>(*([FakeTensor(..., size=(1, 3, 6, 6)), FakeTensor(..., size=(1, 3, 2, 2))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 6 in dimension 2 but got 2 for tensor number 1 in the list

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/ao/nn/quantized/modules/functional_modules.py", line 82, in cat
    r = torch.cat(x, dim=dim)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''