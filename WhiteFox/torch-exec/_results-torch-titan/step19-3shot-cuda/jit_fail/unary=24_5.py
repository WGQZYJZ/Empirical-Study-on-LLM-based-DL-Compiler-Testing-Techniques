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
        self.conv = torch.nn.Conv2d(5, 16, kernel_size=(5,), stride=(2,))

    def forward(self, x):
        v1 = self.conv(x)
        mask = (v1 > 0)
        v2 = (v1 * 0.1)
        v3 = torch.where(mask, v1, v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 5, 40, 80)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected padding to be a single integer value or a list of 1 values to match the convolution dimensions, but got padding=[0, 0]

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 5, 40, 80)),), **{}):
tuple index out of range

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''