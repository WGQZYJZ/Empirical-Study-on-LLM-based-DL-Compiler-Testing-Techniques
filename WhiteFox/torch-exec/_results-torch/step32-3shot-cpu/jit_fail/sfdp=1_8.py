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
        self.w_q = torch.nn.Linear(10, 5)
        self.w_k = torch.nn.Linear(10, 4)
        self.w_v = torch.nn.Linear(10, 6)
        self.w_o = torch.nn.Linear(6, 10)

    def forward(self, query, key, value, dropout_p):
        q = self.w_q(query)
        k = self.w_k(key)
        v = self.w_v(value)
        dk = torch.tensor(q.size(2) * q.size(3) / key.size(2) * key.size(-1) ** (-0.5)).to(q.device)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk * dk
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return self.w_o(output)


func = Model().to('cpu')


query = torch.randn(3, 4, 10)

key = torch.randn(3, 5, 10)

value = torch.randn(3, 5, 10)
dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 3)

jit:
IndexError: tuple index out of range

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''