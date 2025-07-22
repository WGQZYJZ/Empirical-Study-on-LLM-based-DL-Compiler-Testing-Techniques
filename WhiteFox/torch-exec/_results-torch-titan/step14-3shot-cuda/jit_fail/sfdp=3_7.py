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



class Attention(nn.Module):

    def __init__(self, n_in1, n_in2, n_out, dropout_p):
        super().__init__()
        self.linear = nn.Linear(n_in1, n_out)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scale_factor = (n_in2 ** (- 0.5))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = self.dropout(dropout_qk).matmul(value)
        return output




n_in1 = 3


n_in2 = 6


n_out = 1


dropout_p = 0.2

func = Attention(n_in1, n_in2, n_out, dropout_p).to('cuda')

query = 1
key = 1
value = 1

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''