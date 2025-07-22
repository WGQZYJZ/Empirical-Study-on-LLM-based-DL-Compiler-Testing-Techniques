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

    def forward(self, x1, x2, inp1, inp2, inp3, inp4):
        v1 = torch.mm(inp1, inp2)
        v2 = (v1 + x1)
        v3 = torch.mm(v2, inp3)
        v4 = (v3 + inp4)
        return v4




func = Model().to('cuda')



x1 = torch.randn(3, 78)



x2 = torch.randn(3, 78)



inp1 = torch.zeros(1, 78)



inp2 = torch.zeros(1, 78)



inp3 = torch.zeros(3, 78)



inp4 = torch.zeros(1, 3)


test_inputs = [x1, x2, inp1, inp2, inp3, inp4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x78 and 1x78)

jit:
Failed running call_function <built-in method mm of type object at 0x7831edc699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 78)), FakeTensor(..., device='cuda:0', size=(1, 78))), **{}):
a and b must have same reduction dim, but got [1, 78] X [1, 78].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''