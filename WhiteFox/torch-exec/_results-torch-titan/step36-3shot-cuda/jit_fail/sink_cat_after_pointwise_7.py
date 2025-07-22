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
        x = torch.cat([x, x], dim=1).view((- 1), 200)
        x = x.transpose(0, 1).view(x.shape[1:], x.shape[0])




func = Model().to('cuda')



x = torch.randn(3, 512, 16, 16, requires_grad=True)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[-1, 200]' is invalid for input of size 786432

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(3, 1024, 16, 16)), -1, 200), **{}):
shape '[-1, 200]' is invalid for input of size 786432

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''