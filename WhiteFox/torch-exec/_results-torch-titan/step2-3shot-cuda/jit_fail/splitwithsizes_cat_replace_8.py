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
        v1 = torch.split(x1, (2, 8, 8, 2), dim=1)
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=2)
        v3 = torch.split(v2, (2, 4, 2), dim=1)
        v4 = torch.cat([v3[i] for i in range(len(v3))], dim=1)
        return True



func = Model().to('cuda')



x1 = torch.randn(1, 32, 14, 14)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 32 (input tensor's size at dimension 1), but got split_sizes=[2, 8, 8, 2]

jit:
Failed running call_function <function split at 0x7a6eca16f0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 14, 14)), (2, 8, 8, 2)), **{'dim': 1}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''