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

    def __init__(self, num_in, num_out):
        super().__init__()
        self.linear = torch.nn.Linear(num_in, num_out)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v2



num_in = 1
num_out = 1
func = Model((28 * 28), 10).to('cuda')



x1 = torch.randn(5, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (140x28 and 784x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(5, 28, 28)),), **{}):
a and b must have same reduction dim, but got [140, 28] X [784, 10].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''