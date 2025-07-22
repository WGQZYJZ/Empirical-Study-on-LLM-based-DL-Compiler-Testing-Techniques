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

    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2)
        v2 = (v1.reshape(3, 3) + torch.mm(inp, v1))
        return v2




func = Model().to('cuda')



x1 = torch.randn(4, 4, 1, 3, 3)



x2 = torch.randn(4, 4, 1, 3, 3)



inp = torch.randn(3, 4, 1, 3, 3)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7be7576699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 4, 1, 3, 3)), FakeTensor(..., device='cuda:0', size=(4, 4, 1, 3, 3))), **{}):
a must be 2D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''