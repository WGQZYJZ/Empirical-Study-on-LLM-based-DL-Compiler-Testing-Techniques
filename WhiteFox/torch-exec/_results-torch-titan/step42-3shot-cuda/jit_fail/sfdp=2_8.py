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
        self.query = torch.nn.Linear(16, 16)
        self.key = torch.nn.Linear(16, 16)
        self.value = torch.nn.Linear(16, 16)

    def forward(self, q, k, v, mask, dropout=None, scale_factor=1, inv_scale_factor=None):
        q = self.query(q)
        k = self.key(k)
        v = self.value(v)
        (n_k, b, h, _) = q.shape
        (n_k, b, h2, _) = k.shape
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        if (scale_factor > 1):
            scaled_qk = (qk * scale_factor.view(n_k).expand((n_k, n_k)))
        else:
            scaled_qk = qk
        return output



func = Model().to('cuda')



q = torch.randn(1, 16)



k = torch.randn(1, 16)



v = torch.randn(1, 16)

mask = 1

test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
not enough values to unpack (expected 4, got 2)

jit:


from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''