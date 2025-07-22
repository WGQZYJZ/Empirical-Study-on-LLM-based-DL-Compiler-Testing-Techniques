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

    def forward(self, a):
        v0 = torch.cat((a, a), dim=0)
        v1 = v0.view((2, a.size(0), a.size(1))).permute((1, 0, 2)).contiguous().clone()
        v3 = v0.view((a.size(0), (2 * a.size(0)), a.size(1))).permute((1, 0, 2)).contiguous().clone()
        v2 = torch.relu(v1)
        v4 = torch.relu(v3)
        return (v2 * v4.view((- 1)))




func = Model().to('cuda')



a = torch.randn(2, 3)


test_inputs = [a]

# JIT_FAIL
'''
direct:
shape '[2, 4, 3]' is invalid for input of size 12

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(4, 3)), (2, 4, 3)), **{}):
shape '[2, 4, 3]' is invalid for input of size 12

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''