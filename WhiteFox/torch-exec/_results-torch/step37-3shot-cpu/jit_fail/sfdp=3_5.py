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

class Model(nn.Module):

    def __init__(self, num_heads=4, d_model=16, p=0.1):
        super().__init__()
        self.linear = nn.Linear(16, num_heads)
        self.value = nn.Linear(16, d_model)
        self.key = nn.Linear(16, d_model)
        self.query = nn.Linear(16, d_model)
        self.dropout = nn.Dropout(p)

    def forward(self, x1):
        k = self.key(x1)
        q = self.query(x1)
        v = self.value(x1)
        batch_size = k.shape[0]
        d_model = k.shape[1]
        head_dim = d_model // self.linear.out_features
        kh = k.view(batch_size, -1, self.linear.out_features, head_dim)
        qh = q.view(batch_size, -1, self.linear.out_features, head_dim)
        vh = v.view(batch_size, -1, self.linear.out_features, head_dim)
        kh = kh.transpose(-2, -1)
        qh = qh.transpose(-2, -1)
        qk = torch.matmul(qh, kh)
        scale_factor = 1 / math.sqrt(head_dim)
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        out = torch.matmul(dropout_qk, vh).transpose(-2, -1)
        return out.reshape(batch_size, d_model)


func = Model(1, 16, 0.1).to('cpu')


x1 = torch.randn(16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [16, 1] but got: [16, 16].

jit:
Failed running call_function <built-in method matmul of type object at 0x783d08196ec0>(*(FakeTensor(..., size=(16, 1, 16, 1)), FakeTensor(..., size=(16, 1, 16, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [16, 1] but got: [16, 16].

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''