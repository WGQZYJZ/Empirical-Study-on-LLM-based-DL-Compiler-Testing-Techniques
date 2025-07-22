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
        self.conv = torch.nn.Conv2d(2, 2, 1, stride=1, padding=1)

    def forward(self, input_tensor):
        t1 = self.conv(input_tensor)
        t2 = t1 + 3
        t3 = torch.clamp(t2, 0, 6)
        t5 = t3 * t1
        t6 = torch.mm(t5, t3)
        t7 = torch.div(t6, 6)
        return t7



func = Model().to('cpu')


input_tensor = torch.randn(1, 2, 3, 3, requires_grad=True)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x79b024d96ec0>(*(FakeTensor(..., size=(1, 2, 5, 5)), FakeTensor(..., size=(1, 2, 5, 5))), **{}):
a must be 2D

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''