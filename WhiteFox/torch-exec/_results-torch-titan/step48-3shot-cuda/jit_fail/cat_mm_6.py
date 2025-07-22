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
        self.bn6 = torch.nn.BatchNorm2d(20, affine=True, track_running_stats=True)

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        for loopVar1 in range(575):
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.mm(x1, x2)
            v1 = torch.nn.functional.relu(self.bn6(v1))
        return torch.cat([v1, v1], 1)




func = Model().to('cuda')



x1 = torch.randn(3, 400)



x2 = torch.randn(400, 5)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
expected 4D input (got 2D input)

jit:
Failed running call_module L__self___bn6(*(FakeTensor(..., device='cuda:0', size=(3, 5)),), **{}):
expected 4D input (got 2D input)

from user code:
   File "<string>", line 36, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''