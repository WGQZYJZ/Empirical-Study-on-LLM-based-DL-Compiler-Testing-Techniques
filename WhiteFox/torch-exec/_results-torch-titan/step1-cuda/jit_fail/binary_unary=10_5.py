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
        self.linear = torch.nn.Linear(10, 11)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.ones_like(v1)
        return torch.relu((v1 + 0.5), v2)



func = Model().to('cuda')



x = torch.randn(1, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
relu() takes 1 positional argument but 2 were given

jit:
Failed running call_function <built-in method relu of type object at 0x7f73370699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 11)), FakeTensor(..., device='cuda:0', size=(1, 11))), **{}):
relu() takes 1 positional argument but 2 were given

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''