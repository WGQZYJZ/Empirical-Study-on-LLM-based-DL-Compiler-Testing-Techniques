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
        super(Model, self).__init__()

    def forward(self, x):
        t1 = torch.mm(x, x)
        t2 = torch.mm(x, x)
        t3 = t1 + t2
        t4 = torch.mm(x, x)
        t5 = t1 + t2 + t3 + t4
        t6 = torch.mm(x, x)
        t7 = t5 + t6
        t8 = torch.mm(x, x)
        t9 = t6 + t8
        t10 = t7 + t9
        return t10



func = Model().to('cpu')


x = torch.randn(1, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x2 and 1x2)

jit:
Failed running call_function <built-in method mm of type object at 0x740d69b96ec0>(*(FakeTensor(..., size=(1, 2)), FakeTensor(..., size=(1, 2))), **{}):
a and b must have same reduction dim, but got [1, 2] X [1, 2].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''