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
        super(Model, self).__init__()
        conv = nn.Conv2d(3, 6, kernel_size=3, stride=1, padding=1, bias=False)
        bn = nn.BatchNorm2d(3)
        self.layer = nn.Sequential(conv, bn)

    def forward(self, x):
        return self.layer(x)



func = Model().to('cpu')


x = torch.randn(1, 3, 4, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 6 elements not 3

jit:
Failed running call_function <function batch_norm at 0x7c8a8c5ebe50>(*(FakeTensor(..., size=(1, 6, 4, 4)), FakeTensor(..., size=(3,)), FakeTensor(..., size=(3,)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 6 elements not 3

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''