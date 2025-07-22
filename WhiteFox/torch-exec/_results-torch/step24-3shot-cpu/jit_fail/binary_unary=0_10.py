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

    def forward(self, x1):
        v1 = x1.view(1, 256, 1, 1)
        v2 = torch.nn.functional.max_pool2d(v1, 1, stride=1, padding=0, dilation=1, ceil_mode=False)
        v3 = v2.permute(0, 2, 3, 1)
        return v3



func = Model().to('cpu')


x1 = torch.randn((1, 64))

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 256, 1, 1]' is invalid for input of size 64

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 64)), 1, 256, 1, 1), **{}):
shape '[1, 256, 1, 1]' is invalid for input of size 64

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''