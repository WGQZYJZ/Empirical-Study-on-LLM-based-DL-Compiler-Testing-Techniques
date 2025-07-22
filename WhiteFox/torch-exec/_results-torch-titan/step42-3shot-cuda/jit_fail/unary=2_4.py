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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 1, 1, stride=0, padding=0, dilation=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v10 = (v1 * 0.2)
        v11 = ((v1 * v1) * v1)
        v12 = (v11 * 6.8625)
        v13 = (v1 + v12)
        v14 = (v13 * 10.188842994226304)
        v15 = torch.tanh(v14)
        v16 = (v15 + 1)
        v17 = (v1 * 3.2766008787968)
        v9 = (v17 + (v10 * v16))
        return v9




func = Model().to('cuda')



x1 = torch.randn(3, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(3, 3, 32, 32)),), **{}):
non-positive stride is not supported

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''