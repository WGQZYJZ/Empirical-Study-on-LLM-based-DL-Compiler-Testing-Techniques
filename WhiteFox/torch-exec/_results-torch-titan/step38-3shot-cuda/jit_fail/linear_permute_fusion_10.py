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
        self.linear = torch.nn.Linear(2, 2, bias=False).cuda()

    def forward(self, x1):
        v4 = x1
        v3 = v4.view(1)
        v1 = torch.nn.functional.linear(v3, self.linear.weight)
        v2 = v1.permute(0, 2, 1).cuda()
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1]' is invalid for input of size 4

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), 1), **{}):
shape '[1]' is invalid for input of size 4

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''