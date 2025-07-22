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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.alpha = torch.randn(8, 8, 1, 1)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = nn.functional.pad(t1, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0))
        t3 = torch.mul(t2, self.alpha)
        return t3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Padding length should be less than or equal to two times the input dimension but got padding length 12 and input of dimension 4

jit:
Failed running call_function <built-in function pad>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0)), **{}):
Padding length should be less than or equal to two times the input dimension but got padding length 12 and input of dimension 4

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''