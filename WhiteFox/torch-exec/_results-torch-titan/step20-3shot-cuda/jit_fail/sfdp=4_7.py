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
        self.q_linear = torch.nn.Linear((8 * 3), 64)
        self.k_linear = torch.nn.Linear(64, 32)

    def forward(self, x1):
        b = x1.shape[0]
        x1x1 = x1.view([b, (8 * 3)])
        q = self.q_linear(x1x1)
        k = self.k_linear(x1x1)
        attn_map = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        attn_mask = torch.ones([1, 32, 32])
        x1x1 = (attn_map + attn_mask)
        x2 = torch.softmax(x1x1, dim=(- 1))
        x3 = (x1x1 @ k.transpose((- 2), (- 1))).transpose((- 2), (- 1))
        return x3



func = Model().to('cuda')



x1 = torch.randn(1, (64 * 3))


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 24]' is invalid for input of size 192

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 192)), [1, 24]), **{}):
shape '[1, 24]' is invalid for input of size 192

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''