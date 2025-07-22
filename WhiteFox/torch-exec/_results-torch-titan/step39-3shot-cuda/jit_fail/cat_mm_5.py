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
        self.conv1 = torch.nn.Conv2d(2, 5, 1, bias=False)
        self.conv2 = torch.nn.Conv2d(5, 7, 1, bias=False)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        w = list(v2.size())
        w[1] = 1
        return v2.view(tuple(w))




func = Model().to('cuda')



x = torch.randn(2, 2, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[2, 1, 2, 2]' is invalid for input of size 56

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(2, 7, 2, 2)), (2, 1, 2, 2)), **{}):
shape '[2, 1, 2, 2]' is invalid for input of size 56

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''