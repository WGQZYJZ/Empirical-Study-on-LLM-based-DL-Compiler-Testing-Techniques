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
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, k1, q1, v1):
        qk = torch.matmul(q1, k1.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v1)
        return output



func = Model().to('cuda')



k1 = torch.randn(1, 120, 32)



q1 = torch.randn(1, 150, 32)



v1 = torch.randn(1, 130, 24)


test_inputs = [k1, q1, v1]

# JIT_FAIL
'''
direct:
The size of tensor a (120) must match the size of tensor b (8) at non-singleton dimension 2

jit:
Failed running call_method mul(*(FakeTensor(..., device='cuda:0', size=(1, 150, 120)), FakeTensor(..., size=(8,))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([8]); but expected shape should be broadcastable to [1, 150, 120]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''