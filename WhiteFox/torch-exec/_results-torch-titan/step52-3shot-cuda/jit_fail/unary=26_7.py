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
        self.conv_t = torch.nn.ConvTranspose2d(95, 95, 7, bias=False)

    def forward(self, x7):
        v5 = self.conv_t(x7)
        v6 = (v5 > 0)
        v7 = (v5 * (- 1.5))
        v8 = torch.where(v6, v5, v7)
        return v8




func = Model().to('cuda')



x7 = torch.randn(19, 94, 10, 12)


test_inputs = [x7]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [95, 95, 7, 7], expected input[19, 94, 10, 12] to have 95 channels, but got 94 channels instead

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(19, 94, 10, 12)),), **{}):
Given transposed=1, weight of size [95, 95, 7, 7], expected input[19, 94, 10, 12] to have 95 channels, but got 94 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''