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
        self.attention = Attention()

    def forward(self, x1, x2):
        q = x1
        k = x2
        v = x2
        (_, _, v) = self.attention(q, k, v)
        return v




class Attention(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, q, k, v):
        inv_scale_factor = (k.shape[(- 1)] ** (- 0.25))
        dropout_p = 0.1
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return (output, None, None)




func = Attention().to('cuda')



x1 = torch.randn(1, 4, 16)



x2 = torch.randn(1, 4, 16)

q = 1

test_inputs = [x1, x2, q]

# JIT_FAIL
'''
direct:
matmul(): argument 'other' (position 1) must be Tensor, not int

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 4, 4)), 1), **{}):
matmul(): argument 'other' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 43, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''