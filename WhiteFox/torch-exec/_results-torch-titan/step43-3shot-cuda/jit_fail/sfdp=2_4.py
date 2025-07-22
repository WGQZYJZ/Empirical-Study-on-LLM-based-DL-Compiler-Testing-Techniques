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
        self.dropout = torch.nn.Dropout(0.1613765264515159)
        self.linear1 = torch.nn.Linear(3, 32)
        self.linear2 = torch.nn.Linear(32, 10)

    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1)
        v3 = self.dropout(v2)
        v4 = self.linear1(x2)
        v5 = v4.transpose((- 2), (- 1))
        v6 = torch.matmul(v3, v5)
        return v6



func = Model().to('cuda')



x1 = torch.randn(10, 3)



x2 = torch.randn(10, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (10x10 and 32x10)

jit:
Failed running call_function <built-in method matmul of type object at 0x7b27cb4699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 10)), FakeTensor(..., device='cuda:0', size=(32, 10))), **{}):
a and b must have same reduction dim, but got [10, 10] X [32, 10].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''