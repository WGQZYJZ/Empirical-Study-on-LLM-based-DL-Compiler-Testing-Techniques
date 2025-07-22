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
        self.heads = 8
        self.seq_len = 512
        self.dim = (64 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = torch.reshape(qk, (1, (8 * self.seq_len), (512 * self.seq_len)))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=2)
        attn_weight = torch.reshape(attn_weight, (1, 8, self.seq_len, self.seq_len))
        attn_weight = torch.dropout(attn_weight, 0.1, True)
        output = torch.cat([attn_weight for i in range(self.heads)], dim=1)
        output = output.reshape((1, (8 * self.seq_len), self.seq_len))
        ww = (output @ value.transpose((- 2), (- 1)))
        output = ww.reshape((1, 7660, 512))
        return output




func = Model().to('cuda')



query = torch.randn(1, 8, 512, 64)



key = torch.randn(1, 8, 512, 64)



value = torch.randn(1, 8, 512, 64)



attn_mask = torch.randn(1, 1, 512, 512)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
shape '[1, 4096, 262144]' is invalid for input of size 2097152

jit:
Failed running call_function <built-in method reshape of type object at 0x7c28f88699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 512, 512)), (1, 4096, 262144)), **{}):
shape '[1, 4096, 262144]' is invalid for input of size 2097152

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''