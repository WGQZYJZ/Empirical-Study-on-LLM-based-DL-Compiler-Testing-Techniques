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
        self.linear = torch.nn.functional.linear

    def forward(self, x1):
        return self.linear(x1, torch.randn(1, 4, 1, 1))



func = Model().to('cuda')



x1 = torch.randn(1, 3, 24, 24)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 4D

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 24, 24)), FakeTensor(..., size=(1, 4, 1, 1))), **{}):
t() expects a tensor with <= 2 dimensions, but self is 4D

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''