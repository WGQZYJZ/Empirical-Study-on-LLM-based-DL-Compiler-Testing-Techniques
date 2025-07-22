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
        tensorList = []
        for loopVar1 in range(10):
            v = x1.type_as(torch.DoubleTensor()).to(torch.device('cuda:' + str(loopVar1 % 4)))
            v = x1 + (v + torch.randn(torch.Size([1, 3])))
            v = torch.mm(v, v)
            v = torch.mm(v, v)
            v = torch.mm(v, v)
            v = torch.mm(v, v)
            tensorList.append(v.type_as(torch.FloatTensor()).to(torch.device('cuda:0' if loopVar1 % 2 == 0 else 'cuda:1')))
        return torch.cat(tensorList, 0)



func = Model().to('cpu')


x1 = torch.randn(2, 2, requires_grad=True)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(s0, s1), dtype=torch.float64), FakeTensor(..., size=(1, 3))), **{}):
The size of tensor a (s1) must match the size of tensor b (3) at non-singleton dimension 1)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''