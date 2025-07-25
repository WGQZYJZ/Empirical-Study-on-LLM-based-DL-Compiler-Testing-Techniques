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

    def forward(self, query, key, value, inv_scale_factor, dropout_p=0.2):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 1, 128, 1)



key = torch.randn(1, 1, 512, 1)



value = torch.randn(1, 1, 512, 4)



inv_scale_factor = torch.randn(4)


test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
The size of tensor a (512) must match the size of tensor b (4) at non-singleton dimension 3

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(1, 1, 128, 512)), FakeTensor(..., device='cuda:0', size=(4,))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([4]); but expected shape should be broadcastable to [1, 1, 128, 512]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''