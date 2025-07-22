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

    def forward(self, x1, x2, inp1, inp2, inp3):
        v1 = torch.mm(inp1, inp2)
        v2 = (v1 + x1)
        v3 = torch.mm(v2, inp3)
        v4 = torch.mm(v3, x2)
        return v4




func = Model().to('cuda')



x1 = torch.randn(5, 10)



x2 = torch.randn(10, 5)



inp1 = torch.randn(1, 1)



inp2 = torch.randn(1, 1)



inp3 = torch.randn(10, 5)


test_inputs = [x1, x2, inp1, inp2, inp3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x5 and 10x5)

jit:
Failed running call_function <built-in method mm of type object at 0x7831edc699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 5)), FakeTensor(..., device='cuda:0', size=(10, 5))), **{}):
a and b must have same reduction dim, but got [5, 5] X [10, 5].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''