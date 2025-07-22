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
        super(Model, self).__init__()
        a = torch.nn.Conv2d(1, 1, kernel_size=1)

    def forward(self, x1):
        v1 = torch.nn.functional.interpolate(x1, size=[1, 64, 64], mode='nearest')
        v2 = torch.nn.functional.interpolate(v1, size=[1, 64, 64], mode='nearest')
        return v2.permute(0, 2, 1)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input and output must have the same number of spatial dimensions, but got input with spatial dimensions of [8, 8] and output size of [1, 64, 64]. Please provide input tensor in (N, C, d1, d2, ...,dK) format and output size in (o1, o2, ...,oK) format.

jit:
Failed running call_function <function interpolate at 0x72eec5df7430>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 8, 8)),), **{'size': [1, 64, 64], 'mode': 'nearest'}):
Input and output must have the same number of spatial dimensions, but got input with spatial dimensions of [8, 8] and output size of [1, 64, 64]. Please provide input tensor in (N, C, d1, d2, ...,dK) format and output size in (o1, o2, ...,oK) format.

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''