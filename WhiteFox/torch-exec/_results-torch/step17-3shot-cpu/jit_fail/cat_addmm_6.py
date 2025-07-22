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
        self.layers = nn.Linear(3, 10)
        self.batch_norm = nn.BatchNorm1d(5)

    def forward(self, x):
        x = self.layers(x)
        x = torch.cat((x, x, x, x), dim=1)
        x = self.batch_norm(x)
        return x



func = Model().to('cpu')


x = torch.randn(2, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 40 elements not 5

jit:
Failed running call_function <function batch_norm at 0x74c0a0ceae50>(*(FakeTensor(..., size=(s0, 40)), FakeTensor(..., size=(5,)), FakeTensor(..., size=(5,)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 40 elements not 5

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''