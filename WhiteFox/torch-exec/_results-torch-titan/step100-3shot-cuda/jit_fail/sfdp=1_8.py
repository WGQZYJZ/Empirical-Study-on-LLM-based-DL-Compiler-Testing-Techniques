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

    def forward(self, qi, ki, v):
        qk = torch.matmul(qi, ki.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



qi = torch.randn(8, 6, 256)



ki = torch.randn(8, 6, 256)



v = torch.randn(8, 6, 64)


test_inputs = [qi, ki, v]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (16) at non-singleton dimension 2

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(8, 6, 6)), FakeTensor(..., size=(16,))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([16]); but expected shape should be broadcastable to [8, 6, 6]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''