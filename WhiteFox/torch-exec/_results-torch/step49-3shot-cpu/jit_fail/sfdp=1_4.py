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
        self.dropout_qk = torch.nn.Dropout(p=0.4)

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_factor = k.size(-2) ** 0.25
        s_qk = qk.div(inv_scale_factor)
        softmax_qk = s_qk.softmax(dim=-1)
        d_qk = self.dropout_qk(softmax_qk)
        return d_qk.matmul(v)


func = Model().to('cpu')


q = torch.randn(1, 1, 20)

k = torch.randn(1, 1, 20)

v = torch.randn(1, 20, 20)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 1] but got: [1, 20].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(1, 1, 1)), FakeTensor(..., size=(1, 20, 20))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 1] but got: [1, 20].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''