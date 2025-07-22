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
        self.linear = torch.nn.Linear(2000, 1000)

    def forward(self, x):
        y = (x * 4)
        y = y.repeat(1, 2000)
        u = torch.relu(y)
        v = torch.cat((u, u), dim=1)
        w = v.view(8, 2, (- 1))
        x = w.transpose(1, 2)
        return self.linear(x)




func = Model().to('cuda')



x = torch.randn(1, 2000, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Number of dimensions of repeat dims can not be smaller than number of dimensions of tensor

jit:
Failed running call_method repeat(*(FakeTensor(..., device='cuda:0', size=(1, 2000, 1)), 1, 2000), **{}):
Number of dimensions of repeat dims can not be smaller than number of dimensions of tensor

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''