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

    def inv_sqrt(self, x):
        return (1.0 / torch.sqrt(x))

    def forward(self, query, key, scale_factor=1.0, dropout_p=0.1):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        inv_scale_factor = self.inv_sqrt(scale_factor)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(value)



func = Model().to('cuda')



query = torch.randn(5, 6, 20)



key = torch.randn(5, 3, 20)


test_inputs = [query, key]

# JIT_FAIL
'''
direct:
sqrt(): argument 'input' (position 1) must be Tensor, not float

jit:
Failed running call_function <built-in method sqrt of type object at 0x7dd5ed8699e0>(*(1.0,), **{}):
sqrt(): argument 'input' (position 1) must be Tensor, not float

from user code:
   File "<string>", line 25, in forward
  File "<string>", line 21, in inv_sqrt


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''