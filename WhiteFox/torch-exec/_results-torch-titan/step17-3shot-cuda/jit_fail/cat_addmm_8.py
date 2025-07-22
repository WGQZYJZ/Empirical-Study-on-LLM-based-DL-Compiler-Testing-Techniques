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



class Model(nn.Module):

    def forward(self, x):
        x = torch.mm(x, x)
        y = torch.cat([x], dim=1)
        z = torch.cat([y], dim=(- 1))
        return z




func = Model().to('cuda')



x = torch.randn(2, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x4 and 2x4)

jit:
Failed running call_function <built-in method mm of type object at 0x723bcca699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 4)), FakeTensor(..., device='cuda:0', size=(2, 4))), **{}):
a and b must have same reduction dim, but got [2, 4] X [2, 4].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''