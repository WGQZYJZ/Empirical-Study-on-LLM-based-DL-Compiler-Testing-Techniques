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
        self.conv1 = torch.nn.Conv2d(3, 32, 4, stride=4, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 64, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(64, 32, 3, stride=2, padding=0)
        self.conv4 = torch.nn.Conv2d(32, 64, 7, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = torch.add(v2, v4)
        v6 = torch.relu(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 512, 512)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (59) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x72af67796ec0>(*(FakeTensor(..., size=(1, 64, (((s0 - 2)//4)) + 1, (((s1 - 2)//4)) + 1)), FakeTensor(..., size=(1, 64, (((s0 - 2)//8)) - 4, (((s1 - 2)//8)) - 4))), **{}):
The size of tensor a ((((s1 - 2)//4)) + 1) must match the size of tensor b ((((s1 - 2)//8)) - 4) at non-singleton dimension 3)

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''