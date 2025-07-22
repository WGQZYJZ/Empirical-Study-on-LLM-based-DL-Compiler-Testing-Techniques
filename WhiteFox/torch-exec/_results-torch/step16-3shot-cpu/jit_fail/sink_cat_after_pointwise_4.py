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

    def __init(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), dim=2)
        v3 = torch.cat((x2, x2), dim=2)
        v4 = torch.cat((v1, v3), dim=2)
        v5 = torch.cat((v4, v3), dim=2)
        v6 = torch.cat((v1, v5), dim=2)
        v2 = torch.relu(v6)
        v7 = v2.view(-1, 3)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

x2 = torch.randn(1, 2, 3)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
shape '[-1, 3]' is invalid for input of size 44

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, s0, 2*s1 + 6*s3)), -1, 3), **{}):
shape '[-1, 3]' is invalid for input of size s0*(2*s1 + 6*s3)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''