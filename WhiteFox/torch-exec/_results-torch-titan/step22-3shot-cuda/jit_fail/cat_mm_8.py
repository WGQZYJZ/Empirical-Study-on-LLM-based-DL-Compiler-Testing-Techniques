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
        v1 = torch.mm(torch.rand(1, 5), torch.rand(5, 3))
        v2 = torch.mm(torch.rand(1, 3), torch.rand(3, 1))
        for i in range(5):
            k = torch.mm(v1, v2)
        return k




func = Model().to('cuda')



x = torch.rand(2, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3 and 1x1)

jit:
Failed running call_function <built-in method mm of type object at 0x7f0338a699e0>(*(FakeTensor(..., size=(1, 3)), FakeTensor(..., size=(1, 1))), **{}):
a and b must have same reduction dim, but got [1, 3] X [1, 1].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''