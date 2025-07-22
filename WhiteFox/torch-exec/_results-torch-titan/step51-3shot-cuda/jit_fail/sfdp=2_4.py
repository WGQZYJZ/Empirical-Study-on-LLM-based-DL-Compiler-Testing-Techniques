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

    def __init__(self, d):
        super().__init__()

    def forward(self, query, key, value, d):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = (d ** (- 0.5))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(value)
        return output




d = 128

func = Model(d).to('cuda')



query = torch.randn(1, 128, 32)



key = torch.randn(1, 128, 64)



value = torch.randn(1, 128, 64)

d = 1

test_inputs = [query, key, value, d]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 32] but got: [1, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x76e4624699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 128, 32)), FakeTensor(..., device='cuda:0', size=(1, 64, 128))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 32] but got: [1, 64].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''