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
        self.conv_t = torch.nn.ConvTranspose2d(4, 8, 5, stride=1, padding=5, bias=False)

    def forward(self, x1):
        y1 = self.conv_t(x1)
        y2 = (y1 > 0)
        y3 = (y1 * 5.893)
        y4 = torch.where(y2, y1, y3)
        return y4




func = Model().to('cuda')



x1 = torch.randn(1, 4, 1, 7, requires_grad=False)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -5: [1, 8, -5, 1]

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(1, 4, 1, 7)),), **{}):
Trying to create tensor with negative dimension -5: [1, 8, -5, 1]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''