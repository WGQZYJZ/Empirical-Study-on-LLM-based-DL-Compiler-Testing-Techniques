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
        self.up = torch.nn.Upsample(size=(), scale_factor=5)

    def forward(self, x1):
        v1 = self.up(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 64, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
only one of size or scale_factor should be defined

jit:
Failed running call_module L__self___up(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)),), **{}):
only one of size or scale_factor should be defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''