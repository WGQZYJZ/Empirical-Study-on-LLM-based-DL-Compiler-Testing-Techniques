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

    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        v3 = torch.mm(x1, x2)
        v4 = torch.tensor([[5, 0.1], [0.2, 3]])
        v5 = torch.tensor([[[-1, 2], [6, 5]]])
        v6 = torch.tensor([[[-3, 3], [7, 13]]])
        v7 = torch.tensor([[[0], [0]]])
        return v1 + v2 + v3 + v4 + v5 + v6 + v7



func = Model().to('cpu')


x1 = torch.tensor([[14.1, 12.09, 18.75, 14.15], [-2, 0.12, 0.88, -3.03]])

x2 = torch.tensor([[7.8, 5.84, 2.7, 2.41], [-3.44, 2.75, -3.06, -1.7]])

x3 = torch.tensor([[3.1, -0.32, -4.1, 2.73], [-2.22, -2.89, 3.32, 3.26]])

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x4 and 2x4)

jit:
Failed running call_function <built-in method mm of type object at 0x7bc76a196ec0>(*(FakeTensor(..., size=(2, 4)), FakeTensor(..., size=(2, 4))), **{}):
a and b must have same reduction dim, but got [2, 4] X [2, 4].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''