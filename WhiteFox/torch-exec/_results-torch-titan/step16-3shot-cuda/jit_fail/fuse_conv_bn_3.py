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
        self.conv = torch.nn.Conv3d(3, 7, 3)
        self.bn = torch.nn.BatchNorm3d(3, affine=True)

    def forward(self, x1):
        s = self.conv(x1)
        t = self.bn(s)
        return (s * t)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 4, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 7 elements not 3

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 7, 2, 2, 2)),), **{}):
running_mean should contain 7 elements not 3

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''