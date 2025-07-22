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
        pass

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2, x3], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:1.7976931348623157e+308]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 7, 46, 46)



x2 = torch.randn(1, 4, 46, 46)



x3 = torch.randn(1, 16, 46, 46)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
slice indices must be integers or None or have an __index__ method

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 27, 46, 46)), (slice(None, None, None), slice(0, 1.7976931348623157e+308, None))), **{}):
slice indices must be integers or None or have an __index__ method

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''