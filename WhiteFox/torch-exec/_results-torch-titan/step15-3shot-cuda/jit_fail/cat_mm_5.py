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
        return torch.cat([v1], 0)




func = Model().to('cuda')



x1 = torch.randn(9, 4)



x2 = torch.randn(14, 12)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (9x4 and 14x12)

jit:
Failed running call_function <built-in method mm of type object at 0x79d20ac699e0>(*(FakeTensor(..., device='cuda:0', size=(9, 4)), FakeTensor(..., device='cuda:0', size=(14, 12))), **{}):
a and b must have same reduction dim, but got [9, 4] X [14, 12].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''