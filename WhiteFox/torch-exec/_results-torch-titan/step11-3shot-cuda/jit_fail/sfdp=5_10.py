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

    def __init__(self, dim, nb_head, dropout_p):
        super().__init__()
        self.dim = dim
        self.nb_head = nb_head
        self.dropout_p = dropout_p
        self.head_dim = (dim // nb_head)
        self.query = torch.nn.Linear(dim, dim, bias=False)
        self.key = torch.nn.Linear(dim, dim, bias=False)
        self.value = torch.nn.Linear(dim, dim, bias=False)

    def forward(self, xq, xk, xv, attn_mask):
        q = self.query(qv)
        k = self.key(kv)
        v = self.value(xv)
        qk = (q @ k.transpose((- 2), (- 1)))
        qk = (qk / math.sqrt(q.size((- 1))))
        v = (v + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        v = torch.dropout(attn_weight, self.dropout_p, True)
        output = torch.matmul(k, v)
        return output



dim = 1
nb_head = 1
dropout_p = 1
func = Model(2500, 5, 0.5).to('cuda')



xq = torch.randn(16, 37, 2500)



k = torch.randn(48, 37, 2500)



v = torch.randn(48, 37, 2500)



attn_mask = torch.randn(16, 37, 48, requires_grad=False)


test_inputs = [xq, k, v, attn_mask]

# JIT_FAIL
'''
direct:
name 'qv' is not defined

jit:
name 'qv' is not defined

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''