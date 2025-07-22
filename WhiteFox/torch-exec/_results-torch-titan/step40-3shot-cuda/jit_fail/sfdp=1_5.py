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

    def __init__(self, inv_scale_factor):
        super().__init__()
        self.inv_scale_factor = inv_scale_factor

    def forward(self, query, key, value, dropout_p, mask=None):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = (qk / self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



inv_scale_factor = 1

func = Model(inv_scale_factor).to('cuda')



query = torch.randn(1, 1, 50)



key = torch.randn(1, 100, 50)



value = torch.randn(1, 100, 10)


key = torch.randn(1, 100, 50)


query = torch.randn(1, 1, 50)



input_mask = torch.zeros(query.size(0), key.size((- 2))).byte()

dropout_p = 1

test_inputs = [query, key, value, input_mask, dropout_p]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
Failed running call_function <function dropout at 0x7774230208b0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 100)),), **{'p': FakeTensor(..., device='cuda:0', size=(1, 100), dtype=torch.uint8)}):
Boolean value of Tensor with more than one value is ambiguous

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''