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

    def forward(self, x, y, z1, z2):
        a = torch.mm(x, z1)
        b = torch.mm(z2, y)
        c = (a + b)
        return c




func = Model().to('cuda')



x = torch.randn(32, 3)



y = torch.randn(32, 3)



z1 = torch.randn(32, 3)



z2 = torch.randn(32, 3)


test_inputs = [x, y, z1, z2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x3 and 32x3)

jit:
Failed running call_function <built-in method mm of type object at 0x7a40ff6699e0>(*(FakeTensor(..., device='cuda:0', size=(32, 3)), FakeTensor(..., device='cuda:0', size=(32, 3))), **{}):
a and b must have same reduction dim, but got [32, 3] X [32, 3].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''