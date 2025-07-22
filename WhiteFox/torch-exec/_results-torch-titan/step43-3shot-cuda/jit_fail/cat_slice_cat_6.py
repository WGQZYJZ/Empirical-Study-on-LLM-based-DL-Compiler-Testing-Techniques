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

    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2, x3], dim=0)
        t2 = t1[:, 0:9223372036854775807]

        def size(x):
            return x.shape[1]
        t3 = torch.cat([t2[:, 0, 0, 0, 0], t2[:, (size(t2) - 1), 0, 0, 0]], dim=0)
        t4 = torch.cat([t1, t3], dim=1)
        out = t1
        for x in range(t1.shape[0]):
            out[x] *= t1[x]
        p = torch.tensor([6, 5, 8, 7, 4, 1, 2, 0, 3])
        out = torch.index_select(t1, dim=0, index=p)
        return out



func = Model().to('cuda')



x1 = torch.randn(2, 3, 64, 64)



x2 = torch.randn(4, 3, 64, 64)



x3 = torch.randn(3, 3, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
too many indices for tensor of dimension 4

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(9, 3, 64, 64)), (slice(None, None, None), 0, 0, 0, 0)), **{}):
too many indices for tensor of dimension 4

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''