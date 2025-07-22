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

    def forward(self, input1):
        t1 = torch.mm(input1, input1)
        t2 = torch.mm(t1, input1)
        t3 = torch.mm(input1, input1)
        return t2 + t3



func = Model().to('cpu')


input1 = torch.randn(16, 64)

test_inputs = [input1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x64 and 16x64)

jit:
Failed running call_function <built-in method mm of type object at 0x7abc67796ec0>(*(FakeTensor(..., size=(16, 64)), FakeTensor(..., size=(16, 64))), **{}):
a and b must have same reduction dim, but got [16, 64] X [16, 64].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''