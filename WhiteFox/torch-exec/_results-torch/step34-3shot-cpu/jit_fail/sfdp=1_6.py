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
        t1 = x1.view(1, 36, -1)
        t2 = torch.matmul(t1, t1.transpose(-2, -1).float())
        t3 = torch.div(t2.transpose(-2, -1), 8192)
        t4 = t3.softmax(dim=-1)
        t5 = nn.functional.dropout(t4, p=1)
        ans = t5.matmul(t1)
        return ans


func = Model().to('cpu')


x1 = torch.randn(1, 64, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 36, -1]' is invalid for input of size 16384

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 64, s0)), 1, 36, -1), **{}):
shape '[1, 36, -1]' is invalid for input of size 64*s0

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''