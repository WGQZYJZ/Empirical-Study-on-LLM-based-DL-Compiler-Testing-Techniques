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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat((x1, v1), dim=0)
        v3 = self.linear(v2)
        v4 = v3.view([(- 1)])
        v5 = torch.cat((v2, v3, v4), dim=0)
        v6 = v5.reshape(2, 1, 4)
        y = v6.permute(0, 2, 1)
        return y




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 1

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(12, 2, 2)), 2, 1, 4), **{}):
shape '[2, 1, 4]' is invalid for input of size 48

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''