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
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = x1.reshape((1, (- 1)))
        v4 = x2.reshape((1, (- 1)))
        v5 = (v1 * self.linear.weight)
        v6 = torch.addmm(v5, v4, x1, self.linear.bias)
        return v6.reshape(((1,) + x1.size()))




func = Model().to('cuda')



x1 = torch.randn(1, 2)



x2 = torch.randn(1, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
addmm() takes 3 positional arguments but 4 were given

jit:
Failed running call_function <built-in method addmm of type object at 0x76ddf8e699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2)), FakeTensor(..., device='cuda:0', size=(1, 2)), FakeTensor(..., device='cuda:0', size=(1, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(1,), requires_grad=True))), **{}):
addmm() takes 3 positional arguments but 4 were given

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''