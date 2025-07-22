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

    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, torch.rand(6, 10), torch.rand(10, 6))
        v2 = torch.cat([v1], dim=(- 1))
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 3)



x2 = torch.randn(6, 10)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
addmm() takes 3 positional arguments but 4 were given

jit:
Failed running call_function <built-in method addmm of type object at 0x7dc204e699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3)), FakeTensor(..., device='cuda:0', size=(6, 10)), FakeTensor(..., size=(6, 10)), FakeTensor(..., size=(10, 6))), **{}):
addmm() takes 3 positional arguments but 4 were given

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''