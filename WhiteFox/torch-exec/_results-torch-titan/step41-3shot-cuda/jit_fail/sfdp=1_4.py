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
        self.w_qs = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.w_ks = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.v = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        q1 = self.w_qs(x1)
        k1 = self.w_ks(x2)
        v1 = self.v(x2)
        qk = torch.matmul(q1, k1.transpose((- 2), (- 1)))
        scaled_qk = qk.div(10.0)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(v1)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 8, 1, 1], expected input[1, 3, 64, 64] to have 8 channels, but got 3 channels instead

jit:
Failed running call_module L__self___v(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given groups=1, weight of size [8, 8, 1, 1], expected input[1, 3, 64, 64] to have 8 channels, but got 3 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''