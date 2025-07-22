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
        self.conv_t = torch.nn.ConvTranspose2d(3136, 3008, 10, stride=1, padding=0, bias=False)

    def forward(self, x7):
        t1 = self.conv_t(x7)
        t2 = (t1 > 0)
        t3 = (t1 * 0.2570487)
        t4 = torch.where(t2, t1, t3)
        return t4




func = Model().to('cuda')

x7 = 1

test_inputs = [x7]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___conv_t(*(1,), **{}):
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''