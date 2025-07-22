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
        self.sub = nn.Linear(2, 2)

    def forward(self, x):
        x1 = torch.rand(1, 2)
        x2 = torch.rand(2, 2)
        x = self.sub(x).sum() + x1 + torch.einsum('abc,cb->ac', [x2, x2])
        return x



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
einsum(): the number of subscripts in the equation (3) does not match the number of dimensions (2) for operand 0 and no ellipsis was given

jit:
Failed running call_function <function einsum at 0x759d09d7f040>(*('abc,cb->ac', [FakeTensor(..., size=(2, 2)), FakeTensor(..., size=(2, 2))]), **{}):
einsum(): the number of subscripts in the equation (3) does not match the number of dimensions (2) for operand 0 and no ellipsis was given

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''