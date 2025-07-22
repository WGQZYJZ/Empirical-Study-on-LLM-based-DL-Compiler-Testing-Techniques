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

    def forward(self, m1, m2, m3, m4):
        c1 = torch.mm(m1, m2)
        c2 = torch.mm(m3, m4)
        c3 = (c1 + c2)
        return c3




func = Model().to('cuda')



m1 = torch.randn(3, 2)



m2 = torch.randn(3, 2)



m3 = torch.randn(3, 2)



m4 = torch.randn(3, 2)


test_inputs = [m1, m2, m3, m4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 3x2)

jit:
Failed running call_function <built-in method mm of type object at 0x7a40ff6699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 2)), FakeTensor(..., device='cuda:0', size=(3, 2))), **{}):
a and b must have same reduction dim, but got [3, 2] X [3, 2].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''