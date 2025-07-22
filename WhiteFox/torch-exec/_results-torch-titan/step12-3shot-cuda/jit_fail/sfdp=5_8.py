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

    def __init__(self, d_model=512, num_heads=8, dropout_p=0):
        super().__init__()
        self.d_model = d_model
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(dropout_p)
        self.to_qkv = torch.nn.Linear(d_model, (d_model * 3))

    def forward(self, x1, x2, attn_mask):
        (q, k, v) = torch.chunk(self.to_qkv(x1), 3, dim=(- 1))
        q *= (self.d_model ** (- 0.5))
        qk = (q @ k.transpose((- 2), (- 1)))
        qk += attn_mask
        qk = self.softmax(qk)
        qk = self.dropout(qk)
        o = (qk @ v)
        return o



func = Model().to('cuda')



x1 = torch.randn(3, 128, 512)



x2 = torch.randn(2, 1000, 512)



attn_mask = torch.randn(3, 128, 1000)


test_inputs = [x1, x2, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (1000) at non-singleton dimension 2

jit:
Failed running call_function <built-in function iadd>(*(FakeTensor(..., device='cuda:0', size=(3, 128, 128)), FakeTensor(..., device='cuda:0', size=(3, 128, 1000))), **{}):
Attempting to broadcast a dimension of length 1000 at -1! Mismatching argument at index 1 had torch.Size([3, 128, 1000]); but expected shape should be broadcastable to [3, 128, 128]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''