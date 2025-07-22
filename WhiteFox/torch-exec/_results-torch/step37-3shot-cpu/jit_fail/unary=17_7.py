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

    def __init__(self, num_classes=340):
        super(Model, self).__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 3, stride=2, padding=1)
        self.conv1 = torch.nn.ConvTranspose2d(8, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.ConvTranspose2d(8, 4, 3, stride=2, padding=1)
        self.conv3 = torch.nn.ConvTranspose2d(4, 1, 3, stride=1)
        self.dense = nn.Linear(1, num_classes)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = self.conv3(v3)
        v5 = torch.sigmoid(v4)
        v6 = v5.view(v5.shape[0], -1)
        v7 = self.dense(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x16129 and 1x340)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, (4*s0 - 1)*(4*s1 - 1))), Parameter(FakeTensor(..., size=(340, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(340,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, (4*s0 - 1)*(4*s1 - 1)] X [1, 340].

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''