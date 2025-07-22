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

    def forward(self, x1):
        v1 = torch.mean(x1, dim=1)
        v2 = v1.permute(1, 0).contiguous()
        v3 = v2.view(1)
        return (v1, v2, v3)



func = Model().to('cpu')


x1 = torch.ones(2, device='cuda')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 1)

jit:
Failed running call_function <built-in method mean of type object at 0x75b73df96ec0>(*(FakeTensor(..., size=(2,)),), **{'dim': 1}):
Dimension out of range (expected to be in range of [-1, 0], but got 1)

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''