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

    def forward(self, x):
        t1 = x.view(4, 2, 2).sum(dim=2).sum(dim=1)
        t1 = t1.view(-1, 4)
        t2 = torch.cat((t1, t1), dim=1)
        y = torch.log_softmax(t2, dim=1)
        z = t2.cos()
        return (y, z)



func = Model().to('cpu')


x = torch.randn(1, 8, 8)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[4, 2, 2]' is invalid for input of size 64

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, s0, s1)), 4, 2, 2), **{}):
shape '[4, 2, 2]' is invalid for input of size s0*s1

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''