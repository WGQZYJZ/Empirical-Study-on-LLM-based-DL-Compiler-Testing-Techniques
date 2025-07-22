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



class DotProductAttention(nn.Module):

    def __init__(self, dropout_p=0.0):
        super().__init__()
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, query, key, value, scale_factor=None):
        qk = query.matmul(key.transpose((- 1), (- 2)))
        if scale_factor:
            qk = (qk * scale_factor)
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output



func = DotProductAttention(dropout_p=0.1).to('cuda')



q = torch.randn(16, 1, 512)



k = torch.randn(16, 1, 512)



v = torch.randn(16, 10, 512)

query = 1

test_inputs = [q, k, v, query]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [16, 1] but got: [16, 10].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(16, 1, 1)), FakeTensor(..., device='cuda:0', size=(16, 10, 512))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [16, 1] but got: [16, 10].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''