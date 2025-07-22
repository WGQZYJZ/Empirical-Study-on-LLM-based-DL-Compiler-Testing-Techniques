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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)

    def forward(self, x1, x2, other=1, padding1=None, padding2=None):
        v1 = self.conv1(x1)
        if (padding1 == None):
            padding1 = torch.randn(v1.shape)
        v2 = self.conv2(x2, padding1)
        if (padding2 == None):
            padding2 = torch.randn(v2.shape)
        v3 = (v1 + other)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., size=(1, 8, 64, 64))), **{}):
forward() takes 2 positional arguments but 3 were given

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''