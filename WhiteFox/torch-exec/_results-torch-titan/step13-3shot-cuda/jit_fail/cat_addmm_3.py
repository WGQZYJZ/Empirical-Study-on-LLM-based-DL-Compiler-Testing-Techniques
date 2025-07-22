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

    def forward(self, x1, x2):
        v1 = torch.addmm(alpha=1, mat1=x1, mat2=x2)
        v2 = torch.cat([v1], dim=1)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
addmm() missing 3 required positional argument: "input", "mat1", "mat2"

jit:
Failed running call_function <built-in method addmm of type object at 0x7dc204e699e0>(*(), **{'alpha': 1, 'mat1': FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), 'mat2': FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64))}):
addmm() missing 3 required positional argument: "input", "mat1", "mat2"

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''