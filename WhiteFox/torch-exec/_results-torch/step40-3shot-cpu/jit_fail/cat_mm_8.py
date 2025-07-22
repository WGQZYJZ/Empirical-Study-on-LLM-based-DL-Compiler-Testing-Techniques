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
        v = []
        shape1 = x1.size()
        shape2 = x2.size()
        shape3 = x3.size()
        v.append(torch.mm(x1, x2))
        v.append(torch.mm(x1, x2))
        if len(shape1) == 2 or len(shape2) == 2 or len(shape3) == 2:
            v.append(torch.nn.functional.interpolate(x1, (100, 100), mode='bilinear', align_corners=False))
            v.append(torch.nn.functional.interpolate(x1, (105, 105), mode='bilinear', align_corners=False))
        i = 0
        for x in v:
            if i < 4:
                v[i] = x + torch.mm(v[i], v[i])
            i = i + 1
        return torch.cat(v, 1)



func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(3, 3)

x3 = torch.randn(3, 3)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Input and output must have the same number of spatial dimensions, but got input with spatial dimensions of [] and output size of (100, 100). Please provide input tensor in (N, C, d1, d2, ...,dK) format and output size in (o1, o2, ...,oK) format.

jit:
Failed running call_function <function interpolate at 0x785558e040d0>(*(FakeTensor(..., size=(s0, s1)), (100, 100)), **{'mode': 'bilinear', 'align_corners': False}):
Input and output must have the same number of spatial dimensions, but got input with spatial dimensions of [] and output size of (100, 100). Please provide input tensor in (N, C, d1, d2, ...,dK) format and output size in (o1, o2, ...,oK) format.

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''