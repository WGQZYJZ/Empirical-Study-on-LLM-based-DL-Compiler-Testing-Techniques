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
        self.bn = torch.nn.BatchNorm2d(4)

    def forward(self, x1):
        s = torch.nn.functional.conv2d(x1, torch.rand([3, 4, 3, 3], device='cpu'))
        t = torch.nn.functional.batch_norm(s)
        return t




func = Model().to('cuda')



x1 = torch.randn(1, 4, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
Failed running call_function <function batch_norm at 0x7bbc0b0e3b80>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 2, 2)),), **{}):
batch_norm() missing 2 required positional arguments: 'running_mean' and 'running_var'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''