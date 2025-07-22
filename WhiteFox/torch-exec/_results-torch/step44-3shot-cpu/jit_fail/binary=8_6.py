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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.fc = torch.nn.Linear(8 * 32, 16)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = v1 + v2
        v4 = self.conv3(x1)
        v5 = self.conv4(x2)
        v6 = self.conv5(x1) + v4 + v5
        v7 = self.conv5(x1)
        v8 = self.conv5(x2)
        v9 = v8 * v6
        v10 = v7 + v9
        v11 = v10.permute(0, 2, 1, 3)
        v12 = self.fc(v11)
        v13 = v12.permute(0, 1, 3, 2)
        return v13



func = Model().to('cpu')


x1 = torch.randn(4, 3, 32, 32)

x2 = torch.randn(4, 3, 32, 32)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (544x17 and 256x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(4, 17, 8, 17)), Parameter(FakeTensor(..., size=(16, 256), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [544, 17] X [256, 16].

from user code:
   File "<string>", line 36, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''