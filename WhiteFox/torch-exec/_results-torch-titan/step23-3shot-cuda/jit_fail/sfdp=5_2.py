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
        self.dropout = None
        self.heads = 256
        self.seq_len = 1024
        self.dim = (128 // self.heads)

    def forward(self, query, key, value, attn_mask):
        qk = ((query @ key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, self.dropout, True)
        output = (attn_weight @ value)
        return output




func = Model().to('cuda')



query = torch.randn(1, 256, 1024, 128)



key = torch.randn(1, 256, 1024, 128)



value = torch.randn(1, 256, 1024, 128)



attn_mask = torch.randn(1, 1, 1024, 1024)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
dropout(): argument 'p' (position 2) must be float, not NoneType

jit:
Failed running call_function <built-in method dropout of type object at 0x7cf1582699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 256, 1024, 1024)), None, True), **{}):
dropout(): argument 'p' (position 2) must be float, not NoneType

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''