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

    def forward(self, v0, inp):
        x1 = torch.mm(inp, inp)
        x2 = torch.mm(x1, torch.mm(inp, inp))
        x3 = x2.permute(1, 0)
        return (torch.mm(x2, x3) + v0)




func = Model().to('cuda')



inp = torch.randn(8, 1, 3)



v0 = torch.randn(1, 8, 3, requires_grad=True)


test_inputs = [inp, v0]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7786e44699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 3)), FakeTensor(..., device='cuda:0', size=(1, 8, 3))), **{}):
a must be 2D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''