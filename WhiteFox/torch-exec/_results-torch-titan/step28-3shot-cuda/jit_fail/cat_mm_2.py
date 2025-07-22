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

    def forward(self, x):
        v1 = torch.mm(x, x)
        v2 = torch.mm(x, x)
        return torch.cat([v1, v2, v1, v2], 1)




func = Model().to('cuda')



x = torch.randn(4, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x2 and 4x2)

jit:
Failed running call_function <built-in method mm of type object at 0x7f12d7a699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 2)), FakeTensor(..., device='cuda:0', size=(4, 2))), **{}):
a and b must have same reduction dim, but got [4, 2] X [4, 2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''