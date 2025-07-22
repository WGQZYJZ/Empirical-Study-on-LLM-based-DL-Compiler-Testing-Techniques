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

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = (query @ key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = (dropout_qk @ value)
        return output



func = Model().to('cuda')



query = torch.randn(8, 64, 512)



key = torch.randn(4, 1, 512)



value = torch.randn(4, 64, 512)

inv_scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (4) at non-singleton dimension 0

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(8, 64, 512)), FakeTensor(..., device='cuda:0', size=(4, 512, 1))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''