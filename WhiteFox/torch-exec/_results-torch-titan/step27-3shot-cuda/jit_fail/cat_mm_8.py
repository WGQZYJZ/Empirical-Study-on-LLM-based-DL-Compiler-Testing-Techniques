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
        v1 = torch.mm(x2, x2)
        v2 = torch.mm(x2, x2)
        return torch.cat([v1, v2, v1, v2, v1, v2, v1, v2, v1, v2, v1], 1)




func = Model().to('cuda')



x1 = torch.randn(1, 4)



x2 = torch.randn(2, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x1 and 2x1)

jit:
Failed running call_function <built-in method mm of type object at 0x707fef8699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 1)), FakeTensor(..., device='cuda:0', size=(2, 1))), **{}):
a and b must have same reduction dim, but got [2, 1] X [2, 1].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''