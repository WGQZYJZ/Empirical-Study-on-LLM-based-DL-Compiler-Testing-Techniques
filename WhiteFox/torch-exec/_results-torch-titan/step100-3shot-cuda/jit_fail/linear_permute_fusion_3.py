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
        self.conv = torch.nn.Conv2d(1, 2, kernel_size=(3, 3))
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.view(1, 3, 7)
        v3 = self.bn(v2)
        v4 = self.bn(v2)
        v5 = v4.permute(0, 2, 1)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 3, 7]' is invalid for input of size 8

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)), 1, 3, 7), **{}):
shape '[1, 3, 7]' is invalid for input of size 8

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''