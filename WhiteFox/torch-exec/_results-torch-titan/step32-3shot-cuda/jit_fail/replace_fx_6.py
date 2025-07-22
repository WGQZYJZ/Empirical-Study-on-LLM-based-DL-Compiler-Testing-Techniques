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

    def forward(self, input, shape2):
        s1 = torch.nn.functional.dropout(input, p=0.6)
        temp = torch.rand_like(s1)
        c1 = s1.matmul(shape2)
        c2 = torch.nn.functional.dropout(temp)
        return c1




func = Model().to('cuda')



x1 = torch.randn(4, 80)

input = 1

test_inputs = [x1, input]

# JIT_FAIL
'''
direct:
matmul(): argument 'other' (position 1) must be Tensor, not int

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(4, 80)), 1), **{}):
matmul(): argument 'other' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''