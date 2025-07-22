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

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1.view(x1.size(0), 1, (- 1)), x1.view(x1.size(0), (- 1), 1)).view(x1.size(0), (- 1))
        v2 = (v1 + x1.view((- 1)).unsqueeze((- 1)))
        v3 = torch.nn.functional.relu(v2.view((- 1))).view(x1.size())
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 3D

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 12288)), FakeTensor(..., device='cuda:0', size=(1, 12288, 1))), **{}):
t() expects a tensor with <= 2 dimensions, but self is 3D

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''