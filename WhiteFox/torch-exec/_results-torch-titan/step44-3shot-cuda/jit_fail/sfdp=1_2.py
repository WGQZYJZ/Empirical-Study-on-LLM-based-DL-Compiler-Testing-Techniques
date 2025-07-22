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
        self.linear = torch.nn.Linear(64, 256)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        qk = torch.matmul(v1, x2.transpose((- 2), (- 1)))
        inv_scale_factor = (1 / numpy.sqrt(v1.shape[(- 1)]))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        return dropout_qk



func = Model().to('cuda')



x1 = torch.randn(1, 256)



x2 = torch.randn(1, 512, 256)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x256 and 64x256)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 256)),), **{}):
a and b must have same reduction dim, but got [1, 256] X [64, 256].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''