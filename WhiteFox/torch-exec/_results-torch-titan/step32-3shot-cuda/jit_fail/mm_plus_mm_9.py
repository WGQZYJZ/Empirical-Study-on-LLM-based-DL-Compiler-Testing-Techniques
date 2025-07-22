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
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x1)
        v3 = torch.mm(x4, x1)
        return ((v1 + v2) + v3)




func = Model().to('cuda')



x1 = torch.randn(3, 10)



x2 = torch.randn(10, 3)



x3 = torch.randn(5, 5)



x4 = torch.randn(5, 5)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x5 and 3x10)

jit:
Failed running call_function <built-in method mm of type object at 0x7770d92699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 5)), FakeTensor(..., device='cuda:0', size=(3, 10))), **{}):
a and b must have same reduction dim, but got [5, 5] X [3, 10].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''