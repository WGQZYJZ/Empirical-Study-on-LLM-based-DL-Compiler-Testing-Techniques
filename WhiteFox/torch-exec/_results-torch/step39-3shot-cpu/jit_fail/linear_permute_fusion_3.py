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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        conv1 = torch.nn.ConvTranspose2d(2, 2, 2)
        v1 = conv1(x1)
        v2 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x3 and 2x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2, 3)), Parameter(FakeTensor(..., size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 3] X [2, 2].

from user code:
   File "<string>", line 22, in torch_dynamo_resume_in_forward_at_20


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''