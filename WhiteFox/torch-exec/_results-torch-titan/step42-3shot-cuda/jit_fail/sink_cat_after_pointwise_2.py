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

    def forward(self, x):
        y = torch.cat([x, x], dim=1)
        y = torch.cat([y, y], dim=(- 1))
        y = torch.cat([y, y], dim=0)
        y = torch.tanh(y.view((- 1)))
        return (y.view(2, 2) if (y.shape != (4, 2)) else y.view(2, 2))




func = Model().to('cuda')



x = torch.randn(3, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[2, 2]' is invalid for input of size 96

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(96,)), 2, 2), **{}):
shape '[2, 2]' is invalid for input of size 96

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''