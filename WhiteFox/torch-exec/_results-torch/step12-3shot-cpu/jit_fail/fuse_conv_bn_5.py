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
        self.conv0 = torch.nn.Conv2d(4, 8, 3)
        self.bn0 = torch.nn.BatchNorm2d(8)

    def forward(self, x2):
        return self.conv0(self.bn0(x2))



func = Model().to('cpu')


x2 = torch.randn(1, 4, 4, 4)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
running_mean should contain 4 elements not 8

jit:
Failed running call_function <function batch_norm at 0x790fc4caae50>(*(FakeTensor(..., size=(1, 4, 4, 4)), FakeTensor(..., size=(8,)), FakeTensor(..., size=(8,)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 4 elements not 8

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''