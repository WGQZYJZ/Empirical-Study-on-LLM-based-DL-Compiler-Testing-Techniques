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

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        m = torch.cat([v1, v1])
        v2 = torch.mm(m, m)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3, requires_grad=True)



x2 = torch.randn(3, 3, requires_grad=True)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x3 and 6x3)

jit:
Failed running call_function <built-in method mm of type object at 0x7c43320699e0>(*(FakeTensor(..., device='cuda:0', size=(6, 3)), FakeTensor(..., device='cuda:0', size=(6, 3))), **{}):
a and b must have same reduction dim, but got [6, 3] X [6, 3].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''