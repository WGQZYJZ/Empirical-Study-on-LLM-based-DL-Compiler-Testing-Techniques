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

    def forward(self, q, k, v, mask=None):
        q = q.unsqueeze(1)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = (2.7 - (0.7 * random.random()))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1)).masked_fill((mask == 0), (- np.inf))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v.type_as(dropout_qk))
        return output



func = Model().to('cuda')



q = torch.randn(2, 32, 64)



k = torch.randn(2, 32, 64)



v = torch.randn(2, 32, 64)



mask = torch.zeros(2, 32)


test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (32) at non-singleton dimension 2

jit:
Failed running call_method masked_fill(*(FakeTensor(..., device='cuda:0', size=(2, 2, 32, 32)), FakeTensor(..., device='cuda:0', size=(2, 32), dtype=torch.bool), -inf), **{}):
Attempting to broadcast a dimension of length 32 at -2! Mismatching argument at index 1 had torch.Size([2, 2, 32, 32]); but expected shape should be broadcastable to [1, 1, 2, 32]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''