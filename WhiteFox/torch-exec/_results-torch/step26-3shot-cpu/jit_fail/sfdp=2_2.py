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

    def forward(self, input, key, value, mask=None):
        inv_scale_factor = torch.tensor(8.0).log_inverse()
        qk = torch.matmul(input, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(value)
        if mask is not None:
            output = output * mask.unsqueeze(-1)
        return output


func = Model().to('cpu')


input = torch.randn(32, 2, 512)

key = torch.randn(32, 512, 128)

value = torch.randn(32, 512, 128)

mask = torch.randint(0, 2, (32, 1, 128))

test_inputs = [input, key, value, mask]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute 'log_inverse'

jit:
Failed running call_method log_inverse(*(FakeTensor(..., size=()),), **{}):
'FakeTensor' object has no attribute 'log_inverse'

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''