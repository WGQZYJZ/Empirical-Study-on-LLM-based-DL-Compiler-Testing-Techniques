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
        self.conv1 = torch.nn.Conv2d(3, 3, 2)
        self.norm1 = torch.nn.BatchNorm1d(3)

    def forward(self, x1):
        s = self.conv1(x1)
        s = self.conv1(s)
        s = self.norm1(s)
        t = self.norm1(s)
        return s




func = Model().to('cuda')



x1 = torch.randn(1, 3, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected 2D or 3D input (got 4D input)

jit:
Failed running call_module L__self___norm1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 3, 3)),), **{}):
expected 2D or 3D input (got 4D input)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''