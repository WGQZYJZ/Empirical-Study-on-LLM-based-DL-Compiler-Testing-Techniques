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
        x = x.view(-1)
        x = x.view(x.shape[0], 11, 11)
        x = x + x
        x = torch.sum(x, dim=(2, 3), keepdim=True)
        return x



func = Model().to('cpu')


x = torch.randn(1, 15, 25, 50)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[18750, 11, 11]' is invalid for input of size 18750

jit:
Failed running call_method view(*(FakeTensor(..., size=(s0*s1*s2,)), s0*s1*s2, 11, 11), **{}):
shape '[s0*s1*s2, 11, 11]' is invalid for input of size s0*s1*s2

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''