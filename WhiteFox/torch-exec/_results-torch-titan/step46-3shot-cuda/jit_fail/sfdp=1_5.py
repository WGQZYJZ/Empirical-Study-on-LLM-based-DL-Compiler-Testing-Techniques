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

    def __init__(self, dropout_p, d_model, nhead):
        super(Model, self).__init__()
        self.dropout_p = dropout_p
        self.d_model = d_model
        self.nhead = nhead
        self.qk_weight = torch.nn.Parameter(torch.Tensor(d_model, nhead, d_model))
        self.qk_bias = torch.nn.Parameter(torch.Tensor(nhead, d_model))
        self.v_weight = torch.nn.Parameter(torch.Tensor(d_model, nhead, d_model))
        self.v_bias = torch.nn.Parameter(torch.Tensor(nhead, d_model))
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        qk = qk.div(math.sqrt(self.d_model))
        qk = qk.add_(self.qk_bias[:, :, None])
        v = torch.matmul(value, self.v_weight)
        v = v.add_(self.v_bias)
        dropout_qk = self.dropout(torch.nn.functional.softmax(qk, dim=(- 1)))
        output = dropout_qk.matmul(v)
        output = torch.transpose(output, 1, 2)
        return output




dropout_p = 0.1


d_model = 256


nhead = 16

func = Model(dropout_p, d_model, nhead).to('cuda')



d_model = 256


query = torch.randn(1, 128, d_model)



d_model = 256


key = torch.randn(1, 256, d_model)



d_model = 256


value = torch.randn(1, 256, d_model)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (256) at non-singleton dimension 1

jit:
Failed running call_method add_(*(FakeTensor(..., device='cuda:0', size=(1, 128, 256)), FakeTensor(..., device='cuda:0', size=(16, 256, 1), requires_grad=True)), **{}):
Attempting to broadcast a dimension of length 256 at -2! Mismatching argument at index 1 had torch.Size([16, 256, 1]); but expected shape should be broadcastable to [1, 128, 256]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''