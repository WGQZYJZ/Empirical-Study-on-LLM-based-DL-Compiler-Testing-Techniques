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
        t2 = torch.mm(input1.transpose(2, 1), input1)
        return t1 + t2



func = Model().to('cpu')


input1 = torch.randn(216, 27, 10)

test_inputs = [input1]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7776bf796ec0>(*(FakeTensor(..., size=(216, 27, 10)), FakeTensor(..., size=(216, 27, 10))), **{}):
a must be 2D

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''