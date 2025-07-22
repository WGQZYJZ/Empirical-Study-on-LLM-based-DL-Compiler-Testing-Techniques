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
        self.__linear = torch.nn.Linear(8, 8)

    def forward(self, x1, x2=torch.zeros((8, 8))):
        v1 = self.__linear(torch.reshape(x1, (1, 1024))).squeeze(-1)
        return (v1.matmul(x2).matmul(v1).sum(), v1)


func = Model().to('cpu')


x1 = torch.randn(8, 1, 1024)

x2 = torch.randn(2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
shape '[1, 1024]' is invalid for input of size 8192

jit:
Failed running call_function <built-in method reshape of type object at 0x72e20a396ec0>(*(FakeTensor(..., size=(s0, 1, s1)), (1, 1024)), **{}):
shape '[1, 1024]' is invalid for input of size s0*s1

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''