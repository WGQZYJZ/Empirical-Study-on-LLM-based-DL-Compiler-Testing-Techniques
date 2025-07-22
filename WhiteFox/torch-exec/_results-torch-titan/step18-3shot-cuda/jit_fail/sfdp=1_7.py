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
        self.model = torch.nn.Linear(3072, 10, bias=True)

    def forward(self, input, weight):
        v1 = torch.matmul(input, weight.transpose((- 2), (- 1)))
        v2 = (v1 / 0.1)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=0.2)
        return self.model(v4)



func = Model().to('cuda')



input = torch.randn(256, 3072)



weight = torch.randn(2016, 3072)


test_inputs = [input, weight]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (256x2016 and 3072x10)

jit:
Failed running call_module L__self___model(*(FakeTensor(..., device='cuda:0', size=(256, 2016)),), **{}):
a and b must have same reduction dim, but got [256, 2016] X [3072, 10].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''