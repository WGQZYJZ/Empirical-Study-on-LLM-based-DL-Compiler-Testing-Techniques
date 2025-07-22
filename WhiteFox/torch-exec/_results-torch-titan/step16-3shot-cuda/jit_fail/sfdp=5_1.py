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
        self.dropout = 0.1
        self.heads = 32
        self.seq_len = 256
        self.dim = (128 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, self.dropout, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 32, 256, 128)



key = torch.randn(1, 32, 256, 128)



value = torch.randn(1, 32, 256, 128)



attn_mask = torch.randn(1, 1, 256, 64)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (256) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 256, 256)), FakeTensor(..., device='cuda:0', size=(1, 1, 256, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 256, 64]); but expected shape should be broadcastable to [1, 32, 256, 256]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''