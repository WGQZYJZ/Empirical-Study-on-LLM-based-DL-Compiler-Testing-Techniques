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
        size = ((2 - x2.size(1)) // 4)
        if (size > 0):
            v1 = torch.mm(x1, x2)
        else:
            v1 = torch.mm(x2.T, x1.T).T
        v1 = torch.cat([v1, v1, v1, v1], 1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 1)



x2 = torch.randn(2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 1x1)

jit:
Failed running call_function <built-in method mm of type object at 0x7c053f4699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2)), FakeTensor(..., device='cuda:0', size=(1, 1))), **{}):
a and b must have same reduction dim, but got [2, 2] X [1, 1].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''