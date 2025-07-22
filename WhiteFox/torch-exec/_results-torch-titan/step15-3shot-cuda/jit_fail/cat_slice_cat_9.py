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

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2, x3], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:x1.size()[1]]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x3 = torch.randn(1, 1, 1, 1)

x1 = 1
x2 = 1

test_inputs = [x3, x1, x2]

# JIT_FAIL
'''
direct:
expected Tensor as element 1 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x70f9266699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 1, 1, 1)), 1, 1],), **{'dim': 1}):
expected Tensor as element 1 in argument 0, but got int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''