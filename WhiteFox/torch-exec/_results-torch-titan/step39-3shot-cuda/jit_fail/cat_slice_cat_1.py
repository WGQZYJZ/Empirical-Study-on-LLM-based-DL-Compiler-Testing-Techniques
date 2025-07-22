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

    def forward(self, x1, x2, x3, x4):
        t1 = torch.cat([x1, x2, x3, x4], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:65535]
        t4 = torch.cat([t1, t3], dim=1)
        return t4



func = Model().to('cuda')



x2 = torch.randn(1, 8192, 1024, 32)



x3 = torch.randn(1, 65535, 32, 32)



x4 = torch.randn(1, 8192, 32, 64)

x1 = 1

test_inputs = [x2, x3, x4, x1]

# JIT_FAIL
'''
direct:
expected Tensor as element 3 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x7b3f000699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 8192, 1024, 32)), FakeTensor(..., device='cuda:0', size=(1, 65535, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 8192, 32, 64)), 1],), **{'dim': 1}):
expected Tensor as element 3 in argument 0, but got int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''