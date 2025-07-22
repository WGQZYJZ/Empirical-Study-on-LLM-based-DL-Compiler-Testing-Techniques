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

    def __init__(self, v_size):
        super().__init__()
        self.v_size = v_size

    def forward(self, x1):
        (v1, v2) = self.helper(x1)
        return torch.cat([v1, v2, v1, v2, v1, v2, v1, v2, v1, v2, v1, v2, v1, v2, v1, v2], dim=1)

    def helper(self, x1):
        v1 = torch.mm(x1, x1)
        v2 = torch.mm(x1, x1)
        return (v1, v2)



v_size = 1

func = Model(v_size).to('cuda')



x1 = torch.randn(1, 15)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x15 and 1x15)

jit:
Failed running call_function <built-in method mm of type object at 0x7c053f4699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 15)), FakeTensor(..., device='cuda:0', size=(1, 15))), **{}):
a and b must have same reduction dim, but got [1, 15] X [1, 15].

from user code:
   File "<string>", line 22, in forward
  File "<string>", line 26, in helper


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''