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

    def __init__(self, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.query = torch.nn.Linear(4, num_heads)
        self.key = torch.nn.Linear(4, num_heads)
        self.value = torch.nn.Linear(4, num_heads)

    def forward(self, q, k, v):
        queries = self.query(q)
        keys = self.key(k)
        values = self.value(v)
        qk = torch.matmul(queries, keys.transpose((- 2), (- 1)))
        scale_factor = ((self.num_heads // qk.size((- 1))) ** (- 0.25))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.9)
        output = dropout_qk.matmul(values)
        return output



num_heads = 1

func = Model(num_heads).to('cuda')



q = torch.randn(1, 3, 4)



k = torch.randn(1, 2, 4)



v = torch.randn(1, 2, 4)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
0.0 cannot be raised to a negative power

jit:
0.0 cannot be raised to a negative power

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''