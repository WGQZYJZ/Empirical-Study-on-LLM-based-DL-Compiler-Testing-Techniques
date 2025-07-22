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
        self.conv = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = v1.div(1)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=0.2)
        v5 = v4.matmul(1)
        v6 = self.conv(v5)
        return v6



func = Model().to('cuda')



x1 = torch.randn(1, 8, 8, 8)



x2 = torch.randn(1, 8, 8, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
matmul(): argument 'other' (position 1) must be Tensor, not int

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 8, 8, 8)), 1), **{}):
matmul(): argument 'other' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''