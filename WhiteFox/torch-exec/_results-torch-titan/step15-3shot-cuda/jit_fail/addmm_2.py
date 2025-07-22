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
        s = torch.unsqueeze(inp, 1)
        r = torch.unsqueeze(x2, 0)
        v1 = torch.squeeze(torch.mm(r, s), 1)
        v2 = (v1 + x1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(0, 0)



x2 = torch.randn(2, 2)



inp = torch.randn(2, 2)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x77793ae699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., device='cuda:0', size=(2, 1, 2))), **{}):
a must be 2D

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''