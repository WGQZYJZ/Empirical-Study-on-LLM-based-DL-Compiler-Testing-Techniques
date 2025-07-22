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
        self.query = torch.randn(1, 3, 10, 2)
        self.key = torch.randn(1, 3, 20, 2)
        self.value = torch.randn(1, 3, 20, 2)
        self.inv_scale_factor = 30
        self.dropout_p = 0.1

    def forward(self, q, k, v):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return



func = Model().to('cuda')



query = torch.randn(1, 3, 10, 2)



key = torch.randn(1, 3, 20, 2)

q = 1

test_inputs = [query, key, q]

# JIT_FAIL
'''
direct:
name 'inv_scale_factor' is not defined

jit:
name 'inv_scale_factor' is not defined

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''