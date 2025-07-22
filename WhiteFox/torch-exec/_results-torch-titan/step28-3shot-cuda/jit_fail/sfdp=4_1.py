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
        self.wq = torch.nn.Linear(192, 768)
        self.wk = torch.nn.Linear(192, 768)
        self.wv = torch.nn.Linear(192, 192)

    def forward(self, query, key, value, attn_mask):
        q = self.wq(query)
        k = self.wk(key)
        v = self.wv(value)
        v.transpose_(0, 1)
        q = q.unsqueeze(1)
        (_attn_output, attn) = (torch.matmul(q, k.transpose((- 2), (- 1))) / math.sqrt(k.size((- 1))))
        attn = self.mask_attn_softmax(attn, attn_mask)
        output = torch.matmul(attn, v)
        return (output, attn)

    @staticmethod
    def mask_attn_softmax(attn, attn_mask):
        attn = (attn + attn_mask)
        attn = torch.nn.functional.softmax(attn, dim=(- 1))
        return attn



func = Model().to('cuda')



dim_model = 192


tgt_len = 5


positional_encoding_table = torch.zeros(tgt_len, dim_model)



dim_model = 192


tgt_len = 5


query = torch.randn(tgt_len, dim_model)



dim_model = 192


mem_len = 6


memory = torch.randn(mem_len, dim_model)

key = 1

test_inputs = [positional_encoding_table, query, memory, key]

# JIT_FAIL
'''
direct:
too many values to unpack (expected 2)

jit:
Failed running call_function <built-in method matmul of type object at 0x7b58498699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 5)), FakeTensor(..., device='cuda:0', size=(192, 6))), **{}):
a and b must have same reduction dim, but got [1, 5] X [192, 6].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''