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
        self.linear = torch.nn.Linear(64, 32, bias=False)

    def forward(self, x1):
        v1 = self.linear(x1.view(512))
        v2 = v1 > 0
        v3 = v1 * 0.01
        v4 = torch.where(v2, v1, v3)
        return v4


func = Model().to('cpu')


x1 = torch.randn(512, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[512]' is invalid for input of size 32768

jit:
Failed running call_method view(*(FakeTensor(..., size=(512, 64)), 512), **{}):
shape '[512]' is invalid for input of size 32768

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''