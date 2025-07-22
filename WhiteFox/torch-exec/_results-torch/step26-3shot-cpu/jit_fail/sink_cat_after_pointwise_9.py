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
        x1 = torch.cat((x1, x1), dim=-1)
        x1 = x1.view(2, 3, 4)
        return x1.relu()



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[2, 3, 4]' is invalid for input of size 8

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 2, 4)), 2, 3, 4), **{}):
shape '[2, 3, 4]' is invalid for input of size 8

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''