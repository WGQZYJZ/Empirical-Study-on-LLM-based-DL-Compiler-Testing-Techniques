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

    def forward(self, t1, t2):
        tt1 = torch.mm(t1, t1)
        tt2 = torch.mm(t2, t2)
        tt3 = torch.mm(tt1, tt2) + 12
        return tt1.mm(tt2) + tt3



func = Model().to('cpu')


t1 = torch.randn(1, 1, 1, 100, 100)

t2 = torch.randn(1, 1, 1, 100, 100)

test_inputs = [t1, t2]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x75464af96ec0>(*(FakeTensor(..., size=(1, 1, 1, s0, s1)), FakeTensor(..., size=(1, 1, 1, s0, s1))), **{}):
a must be 2D

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''