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

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11):
        x1 = torch.cat([x2, x3], dim=1)
        x2 = x1[:, 0:4611686018427387903]
        x3 = torch.cat([x4, x5], dim=1)
        x4 = x3[:, 0:4611686018427387903]
        x5 = torch.cat([x6, x7], dim=1)
        x6 = x5[:, 0:4611686018427387903]
        x7 = torch.cat([x8, x9], dim=1)
        x8 = x7[:, 0:4611686018427387903]
        x9 = torch.cat([x10, x11], dim=1)
        x10 = x9[:, 0:4611686018427387903]
        x11 = torch.cat([x1, x2], dim=1)
        return x11



func = Model().to('cuda')

x1 = 1
x2 = 1
x3 = 1
x4 = 1
x5 = 1
x6 = 1
x7 = 1
x8 = 1
x9 = 1
x10 = 1
x11 = 1

test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x703cc16699e0>(*([1, 1],), **{'dim': 1}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''