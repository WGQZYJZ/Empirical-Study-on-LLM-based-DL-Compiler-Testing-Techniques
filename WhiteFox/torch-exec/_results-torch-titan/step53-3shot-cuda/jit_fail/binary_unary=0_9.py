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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, v, x0, x1):
        q1 = v[0].cuda()
        q2 = v[1][0].cuda()
        v1 = self.conv1(q1)
        v2 = (v1 + q2)
        v3 = torch.relu(v2)
        v4 = self.conv2(v3)
        a1 = self.conv2(q2)
        v5 = (v4 + a1)
        v6 = torch.relu(v5)
        v7 = self.conv3(v6)
        v8 = (v7 + v[2].cuda())
        v9 = torch.relu(v8)
        v10 = self.conv1(v9)
        v11 = (v10 + q1)
        v12 = torch.relu(v11)
        return v12




func = Model().to('cuda')



x = torch.randn(1, 16, 64, 64)

v = 1
x0 = 1

test_inputs = [x, v, x0]

# JIT_FAIL
'''
direct:
index 1 is out of bounds for dimension 0 with size 1

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)), 1), **{}):
index 1 is out of bounds for dimension 0 with size 1

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''