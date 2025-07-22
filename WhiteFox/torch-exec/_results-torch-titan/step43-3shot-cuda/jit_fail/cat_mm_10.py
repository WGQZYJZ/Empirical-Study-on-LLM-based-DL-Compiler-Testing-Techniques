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
        v2 = torch.mm(x1, x2)
        v3 = torch.mm(torch.cat([v1, v2], 1), torch.cat([v1, v2], 1))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 2)



x2 = torch.randn(2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x4 and 1x4)

jit:
Failed running call_function <built-in method mm of type object at 0x7275948699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 4)), FakeTensor(..., device='cuda:0', size=(1, 4))), **{}):
a and b must have same reduction dim, but got [1, 4] X [1, 4].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''