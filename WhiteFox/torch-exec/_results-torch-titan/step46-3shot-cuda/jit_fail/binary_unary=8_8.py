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
        self.conv1 = torch.nn.Conv2d(3, 8, 2, stride=2, padding=1, groups=1, bias=True)
        self.conv2 = torch.nn.Conv2d(1, 1, 1, stride=1, padding=1, groups=1, bias=True)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1.flatten(1)
        v3 = self.conv1(x1)
        v4 = v3.flatten(1)
        v5 = self.conv1(x1)
        v6 = v5.flatten(1)
        v7 = ((v2 + v4) + v6)
        v8 = self.conv2(v7.reshape(v2.size(0), (- 1), 16, 16))
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, -1, 16, 16]' is invalid for input of size 648

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 648)), 1, -1, 16, 16), **{}):
shape '[1, -1, 16, 16]' is invalid for input of size 648

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''