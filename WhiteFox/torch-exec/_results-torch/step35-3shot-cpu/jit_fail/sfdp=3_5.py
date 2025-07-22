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

    def __init__(self, feature_dim=512, num_heads=8):
        super().__init__()
        self.q = torch.nn.Linear(feature_dim, feature_dim)
        self.k = torch.nn.Linear(feature_dim, feature_dim)
        self.v = torch.nn.Linear(feature_dim, feature_dim)

    def forward(self, x):
        q = self.q(x)
        k = self.k(x)
        v = self.v(x)
        (q, k, v) = [x.view(x.size(0), x.size(1), num_heads, -1) for x in [q, k, v]]
        (q, k, v) = [x.transpose(1, 2) for x in [q, k, v]]
        qk = torch.matmul(q, k)
        scale_factor = (k.size(-1) / qk.size(-1)) ** (-0.5)
        softmax_qk = F.softmax(qk * scale_factor, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=dropout_rate)
        output = torch.matmul(dropout_qk, v)
        output = output.transpose(1, 2)
        output = output.contiguous()
        output = output.view(output.size(0), output.size(1), -1)
        return output


func = Model(feature_dim=512, num_heads=8).to('cpu')


x = torch.randn(16, 64, 512)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [16, 512] but got: [16, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x75a5f4b96ec0>(*(FakeTensor(..., size=(16, 1, 64, 512)), FakeTensor(..., size=(16, 1, 64, 512))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [16, 512] but got: [16, 64].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''