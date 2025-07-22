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
        self.heads = 16
        self.seq_len = 16384
        self.dim = 1
        self.embed_dim = 16384

    def forward(self, query, key, value):
        attn_mask = torch.cat([torch.triu(torch.ones(self.seq_len, self.seq_len, dtype=torch.bool), 1), torch.tril(torch.ones(self.seq_len, self.seq_len, dtype=torch.bool))], dim=(- 1))
        attn_mask = attn_mask.view(1, 1, self.seq_len, self.seq_len)
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, 0.31881923790897965, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 16384, 1, 1)



key = torch.randn(1, 16384, 1, 1)



value = torch.randn(1, 16384, 1, 1)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
shape '[1, 1, 16384, 16384]' is invalid for input of size 536870912

jit:
Failed running call_method view(*(FakeTensor(..., size=(16384, 32768), dtype=torch.bool), 1, 1, 16384, 16384), **{}):
shape '[1, 1, 16384, 16384]' is invalid for input of size 536870912

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''