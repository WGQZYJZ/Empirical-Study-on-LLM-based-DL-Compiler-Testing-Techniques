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
        self.conv_transpose = torch.nn.ConvTranspose1d(50, 100, kernel_size=(21,), stride=(1,), dilation=(2,), groups=1, bias=False, padding=(49,))

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 + 3)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v4 / 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(100, 50, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -57: [100, 100, 1, -57]

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(100, 50, 1)),), **{}):
Trying to create tensor with negative dimension -57: [100, 100, -57]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''