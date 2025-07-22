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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3)
        v3 = v2[:, :, :, ::(- 1)]
        v4 = v3[:, :, :, ::(- 1)]
        v5 = v3[:, :, :, ::(- 1)]
        v6 = v4[:, :, :, ::(- 1)]
        v7 = v5[:, :, :, ::(- 1)]
        v8 = v7[:, :, :, ::(- 1)]
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
step must be greater than zero

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), (slice(None, None, None), slice(None, None, None), slice(None, None, None), slice(None, None, -1))), **{}):
step must be greater than zero

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''