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
        self.heads = 96
        self.seq_len = 2048
        self.dim = (32 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 96, 512, 256)



key = torch.randn(1, 96, 512, 256)



value = torch.randn(1, 96, 512, 256)



attn_mask = torch.randn(1, 1, 2048, 2048)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (512) must match the size of tensor b (2048) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 96, 512, 512)), FakeTensor(..., device='cuda:0', size=(1, 1, 2048, 2048))), **{}):
Attempting to broadcast a dimension of length 2048 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 2048, 2048]); but expected shape should be broadcastable to [1, 96, 512, 512]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''