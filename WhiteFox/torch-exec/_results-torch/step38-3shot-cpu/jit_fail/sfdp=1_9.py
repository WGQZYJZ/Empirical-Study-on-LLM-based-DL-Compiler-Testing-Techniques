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

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        s1 = qk.flatten(2).transpose(-2, -1)
        s2 = s1.div(4)
        s3 = torch.nn.functional.softmax(s2, dim=-1)
        d1 = torch.nn.functional.dropout(s3, p=0.005)
        o1 = d1.transpose(-2, -1).matmul(x1.flatten(2))
        o2 = o1.transpose(-2, -1).contiguous().view(1, 1, 2, 2)
        return o2


func = Model().to('cpu')


x1 = torch.randn(1, 2, 4)

x2 = torch.randn(1, 2, 4)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
shape '[1, 1, 2, 2]' is invalid for input of size 8

jit:
Failed running call_method view(*(FakeTensor(..., size=(1, 4, 2)), 1, 1, 2, 2), **{}):
shape '[1, 1, 2, 2]' is invalid for input of size 8

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''