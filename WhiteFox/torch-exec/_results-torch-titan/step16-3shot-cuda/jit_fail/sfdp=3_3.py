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
        self.matmul1 = torch.nn.Linear(128, 128, bias=False)
        self.matmul2 = torch.nn.Linear(128, 128, bias=False)

    def forward(self, x1, x2):
        v1 = self.matmul1(x1).softmax((- 1)).matmul(x2)
        v2 = self.matmul2(v1)
        return v2



func = Model().to('cuda')



x1 = torch.randn(64, 128)



x2 = torch.randn(64, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x128 and 64x128)

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(64, 128)), FakeTensor(..., device='cuda:0', size=(64, 128))), **{}):
a and b must have same reduction dim, but got [64, 128] X [64, 128].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''