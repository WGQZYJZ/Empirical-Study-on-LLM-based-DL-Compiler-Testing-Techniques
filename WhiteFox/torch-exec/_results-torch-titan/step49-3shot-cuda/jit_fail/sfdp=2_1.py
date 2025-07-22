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

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = ...
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        p = ...
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(2, 128, 16)



key = torch.randn(2, 128, 16)



value = torch.randn(2, 128, 16)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
div(): argument 'other' (position 1) must be Tensor, not ellipsis

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(2, 128, 128)), Ellipsis), **{}):
div(): argument 'other' (position 1) must be Tensor, not ellipsis

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''