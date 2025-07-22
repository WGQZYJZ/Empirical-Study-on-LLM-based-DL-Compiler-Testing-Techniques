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

    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x3)
        v2 = torch.mm(x1, x4)
        v3 = torch.mm(x2, x3)
        v4 = torch.mm(x2, x4)
        v5 = (torch.add(v1, v3) + v2)
        v6 = (torch.add(v1, v2) + v3)
        return (torch.add(v4, v5) + torch.add(v3, v6))




func = Model().to('cuda')



x1 = torch.randn(16, 64)



x2 = torch.randn(16, 64)



x3 = torch.randn(16, 64)



x4 = torch.randn(16, 64)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x64 and 16x64)

jit:
Failed running call_function <built-in method mm of type object at 0x7822a94699e0>(*(FakeTensor(..., device='cuda:0', size=(16, 64)), FakeTensor(..., device='cuda:0', size=(16, 64))), **{}):
a and b must have same reduction dim, but got [16, 64] X [16, 64].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''