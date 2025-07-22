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



class CustomModule(torch.nn.Module):

    def __init__(self, inplace=False):
        super(CustomModule, self).__init__()
        self.inplace = inplace

    def forward(self, x):
        return torch.nn.functional.linear(x, torch.ones(4, 4, device=x.device), self.inplace)



func = CustomModule(inplace=False).to('cuda')



x = torch.randn(2, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
linear(): argument 'bias' (position 3) must be Tensor, not bool

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(2, 4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), False), **{}):
linear(): argument 'bias' (position 3) must be Tensor, not bool

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''