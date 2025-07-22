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
        self.linear = torch.nn.Linear(2, 4)

    def forward(self, x3):
        v3 = x3
        for i in range(2):
            if i == 0:
                v0 = v3
                v1 = torch.nn.functional.linear(v0, self.linear.weight, self.linear.bias)
                v2 = v1.permute(0, 1, 3, 2)
                v3 = v2.contiguous()
            v3.detach_()
        return v3



func = Model().to('cpu')


x3 = torch.randn(1, 2, 2)

test_inputs = [x3]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 3 is not equal to len(dims) = 4

jit:
Failed running call_method permute(*(FakeTensor(..., size=(1, 2, 4)), 0, 1, 3, 2), **{}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''