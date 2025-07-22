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

    def __init__(self, n_q, n_k, d_qk, d_v, dropout_p=0.0):
        super().__init__()
        self.n_q = n_q
        self.n_k = n_k
        self.d_qk = d_qk
        self.d_v = d_v
        self.dropout_p = dropout_p

    def forward(self, query, key, value, scale=1.0):
        v_query = query.view((- 1), (self.n_q * self.d_qk))
        v_key = key.view((- 1), (self.n_k * self.d_qk))
        v_value = value.view((- 1), (self.n_k * self.d_v))
        v_qk = torch.matmul(v_query, v_key.transpose((- 2), (- 1)))
        v_scaled_qk = v_qk.div(scale)
        v_softmax_qk = torch.nn.functional.softmax(v_scaled_qk, dim=(- 1))
        v_dropout_qk = torch.nn.functional.dropout(v_softmax_qk, p=self.dropout_p)
        v_output = torch.matmul(v_dropout_qk, v_value)
        v_output = v_output.view((query.shape[:(- 1)] + ((- 1),)))
        return v_output



n_q = 1
n_k = 1
d_qk = 1
d_v = 1

func = Model(n_q, n_k, d_qk, d_v).to('cuda')



q = torch.randn(3, 80, 8)



k = torch.randn(3, 160, 4)



v = torch.randn(3, 160, 8)

query = 1

test_inputs = [q, k, v, query]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1920x1920 and 3840x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x707c4ba699e0>(*(FakeTensor(..., device='cuda:0', size=(1920, 1920)), FakeTensor(..., device='cuda:0', size=(3840, 1))), **{}):
a and b must have same reduction dim, but got [1920, 1920] X [3840, 1].

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''