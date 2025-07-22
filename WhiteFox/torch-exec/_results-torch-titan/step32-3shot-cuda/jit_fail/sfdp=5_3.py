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
        self.heads = 64
        self.seq_len = 128
        self.dim = 1

    def forward(self, query, key, value, attn_mask, bias=None):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, 0.2, True)
        output = (attn_weight @ value)
        output = output.__neg__()
        if (bias is not None):
            output += (query + torch.softmax(bias.unsqueeze(1).unsqueeze(0), dim=(- 1)))
        return output




func = Model().to('cuda')






query = torch.nn.parameter.Parameter(torch.randn_like(torch.rand(1, 64, 128, 1))).to(torch.int64)






key = torch.nn.parameter.Parameter(torch.randn_like(torch.rand(1, 64, 128, 1))).to(torch.int64)






value = torch.nn.parameter.Parameter(torch.randn_like(torch.rand(1, 64, 128, 1))).to(torch.int64)



attn_mask = torch.randn(1, 1, 128, 128)





bias = torch.nn.parameter.Parameter(torch.randn_like(torch.rand(64)))


test_inputs = [query, key, value, attn_mask, bias]

# JIT_FAIL
'''
direct:
"baddbmm_cuda" not implemented for 'Long'

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 128, 1), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(1, 64, 1))), **{}):
Attempting to broadcast a dimension of length 64 at -2! Mismatching argument at index 1 had torch.Size([1, 64, 1]); but expected shape should be broadcastable to [1, 64, 128, 1]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''