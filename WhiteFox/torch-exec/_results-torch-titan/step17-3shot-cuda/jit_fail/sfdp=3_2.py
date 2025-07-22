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

    def forward(self, q, k, v, scale_factor, dropout_p):
        scale_factor = q[:, 0::(q.size(1) // 4)].reshape(q.shape[0], (- 1)).contiguous()
        dropout_p = q[:, (q.shape[1] // 4):((q.shape[1] * 3) // 4)].reshape(q.shape[0], (- 1)).contiguous()
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor.to(k.dtype).to(qk.device))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        dropout_qk_value = dropout_qk.matmul(v)
        return dropout_qk_value



func = Model().to('cuda')



q = torch.randn(2, 8, 16)



k = torch.randn(2, 8, 16)



v = torch.randn(2, 8, 32)



scale_factor = torch.randn(2)



dropout_p = torch.randn(2)


test_inputs = [q, k, v, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (64) at non-singleton dimension 2

jit:
Failed running call_method mul(*(FakeTensor(..., device='cuda:0', size=(2, 8, 8)), FakeTensor(..., device='cuda:0', size=(2, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([2, 64]); but expected shape should be broadcastable to [2, 8, 8]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''