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



class m1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.mm(x1, x1)
        x3 = torch.randint(0, 9, (1,))
        x4 = torch.rand_like(x2)
        return torch.nn.functional.dropout(x2)




func = m1().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x7967ba0699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 2, 2))), **{}):
a must be 2D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''