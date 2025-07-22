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
        self.bn1 = torch.nn.BatchNorm2d(3, affine=False)
        self.bn2 = torch.nn.BatchNorm2d(3, affine=True)
        self.bn3 = torch.nn.BatchNorm2d(2, affine=False)
        self.relu = torch.nn.ReLU(inplace=True)

    def forward(self, x):
        x1 = self.conv1(x)
        y1 = self.bn1(x1)
        y2 = self.relu(self.bn2(y1))
        y3 = self.relu(self.bn3(self.relu(y2)))
        return y3



func = Model().to('cpu')


x1 = torch.randn(3, 3, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 3 elements not 2

jit:
Failed running call_function <function batch_norm at 0x723d13d2ce50>(*(FakeTensor(..., size=(3, 3, 2, 2)), FakeTensor(..., size=(2,)), FakeTensor(..., size=(2,)), None, None, False, 0.1, 1e-05), **{}):
running_mean should contain 3 elements not 2

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''