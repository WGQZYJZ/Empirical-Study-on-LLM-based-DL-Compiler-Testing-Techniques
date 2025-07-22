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

    def forward(self, x1, x4, x2, v0):
        v1 = torch.mm(x1, x4)
        v3 = torch.mm(x2, x1)
        v2 = (v1 + v3)
        return (v2 + v0)




func = Model().to('cuda')



x1 = torch.randn(3, 2)



x2 = torch.randn(3, 2, requires_grad=True)



x4 = torch.randn(3, 2, requires_grad=True)



v0 = torch.randn(3, 2)


test_inputs = [x1, x2, x4, v0]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 3x2)

jit:
Failed running call_function <built-in method mm of type object at 0x7786e44699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 2)), FakeTensor(..., device='cuda:0', size=(3, 2))), **{}):
a and b must have same reduction dim, but got [3, 2] X [3, 2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''