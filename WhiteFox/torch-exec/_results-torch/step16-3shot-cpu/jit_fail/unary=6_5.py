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
        self.conv = torch.nn.Conv2d(3, 4, 3, stride=3, padding=1)
        self.conv1 = torch.nn.Conv2d(4, 4, 2, stride=1, padding=0)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = self.conv1(t1)
        t3 = t2.clamp(0, 6)
        t4 = t1 * t3
        t5 = t4 / 6
        return t5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (22) must match the size of tensor b (21) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(1, 4, 22, (((s1 - 1)//3)) + 1)), FakeTensor(..., size=(1, 4, 21, ((s1 - 1)//3)))), **{}):
The size of tensor a ((((s1 - 1)//3)) + 1) must match the size of tensor b (((s1 - 1)//3)) at non-singleton dimension 3)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''