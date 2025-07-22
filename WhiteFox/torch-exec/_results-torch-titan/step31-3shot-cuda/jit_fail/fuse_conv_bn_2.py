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
        self.a = torch.nn.BatchNorm1d(16)

    def forward(self, x):
        x = self.a(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 16, 1, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
expected 2D or 3D input (got 4D input)

jit:
Failed running call_module L__self___a(*(FakeTensor(..., device='cuda:0', size=(2, 16, 1, 1)),), **{}):
expected 2D or 3D input (got 4D input)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''