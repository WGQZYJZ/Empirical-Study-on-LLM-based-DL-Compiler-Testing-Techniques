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
        self.deconv = torch.nn.ConvTranspose2d(8, 8, kernel_size=9, stride=9, padding=9)

    def forward(self, x):
        out = self.deconv(x)
        out = torch.sigmoid(out)
        return out




func = Model().to('cuda')



x = torch.randn(1, 8, 1, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -9: [1, 8, -9, -9]

jit:
Failed running call_module L__self___deconv(*(FakeTensor(..., device='cuda:0', size=(1, 8, 1, 1)),), **{}):
Trying to create tensor with negative dimension -9: [1, 8, -9, -9]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''