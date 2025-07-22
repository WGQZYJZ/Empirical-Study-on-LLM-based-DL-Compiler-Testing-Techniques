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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 2, (3, 4), True)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 1, 10, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'stride' (position 4) must be tuple of ints, but found element of type bool at pos 0

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 1, 10, 8)),), **{}):
conv_transpose2d(): argument 'stride' (position 4) must be tuple of ints, but found element of type bool at pos 0

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''