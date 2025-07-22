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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1, 1, 1, 1, 1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(1, 1, 2, 2, (0, 1))
        self.conv_transpose3 = torch.nn.ConvTranspose2d(1, 1, 2, 2, (1, 0), 1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = self.conv_transpose3(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 1, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -1: [1, 1, -1, -1]

jit:
Failed running call_module L__self___conv_transpose1(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 1)),), **{}):
Trying to create tensor with negative dimension -1: [1, 1, -1, -1]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''