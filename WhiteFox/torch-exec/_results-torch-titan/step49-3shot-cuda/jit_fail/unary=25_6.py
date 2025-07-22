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

    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0)
        v3 = (v1 * self.negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4



negative_slope = 1

func = Model(negative_slope).to('cuda')



seq_len = 8


seq_len = 8


batch_size = 2


x1 = torch.randn(batch_size, seq_len, seq_len)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (16x8 and 5x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(2, 8, 8)),), **{}):
a and b must have same reduction dim, but got [16, 8] X [5, 10].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''