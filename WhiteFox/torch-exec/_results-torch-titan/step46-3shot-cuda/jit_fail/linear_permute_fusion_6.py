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
        v2 = [2, 5, 2]
        v1 = torch.zeros(([1] + v2))
        self.register_parameter('weight', torch.nn.Parameter(v1))

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.weight, None)
        v2 = v1.permute(0, 2, 1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(2, 3, 2, device='cpu')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 4D

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 2, 5, 2), requires_grad=True)), None), **{}):
t() expects a tensor with <= 2 dimensions, but self is 4D

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''