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
        self.linear = torch.nn.Linear(5, 5, bias=False)

    def forward(self, t1, t2, t3):
        t4 = self.linear(t2)
        t5 = torch.einsum('bqa,bbqc->bqc', t1, t4)
        t6 = t3 + t5
        return t6


func = Model().to('cpu')


t1 = torch.randn(1, 5, 10, 20)

t2 = torch.randn(8, 5)

t3 = torch.randn(1, 5, 10, 20)

test_inputs = [t1, t2, t3]

# JIT_FAIL
'''
direct:
einsum(): the number of subscripts in the equation (3) does not match the number of dimensions (4) for operand 0 and no ellipsis was given

jit:
Failed running call_function <function einsum at 0x7e25c9541040>(*('bqa,bbqc->bqc', FakeTensor(..., size=(1, 5, 10, 20)), FakeTensor(..., size=(8, 5))), **{}):
einsum(): the number of subscripts in the equation (3) does not match the number of dimensions (4) for operand 0 and no ellipsis was given

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''