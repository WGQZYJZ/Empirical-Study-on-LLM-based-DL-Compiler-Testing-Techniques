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
        self.softmax = torch.nn.Softmax(2)

    def forward(self, x1):
        v1 = self.softmax(x1, 1)
        v2 = (v1 - 192)
        v3 = F.relu(v2)
        v4 = torch.squeeze(v3, 0)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 192, 35, 45)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
Failed running call_module L__self___softmax(*(FakeTensor(..., device='cuda:0', size=(1, 192, 35, 45)), 1), **{}):
forward() takes 2 positional arguments but 3 were given

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''