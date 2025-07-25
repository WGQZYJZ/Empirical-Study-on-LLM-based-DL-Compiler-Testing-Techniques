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

    def __init__(self, d_model):
        super().__init__()
        self.w_1 = torch.nn.Linear(d_model, d_model)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(0.1)
        self.w_2 = torch.nn.Linear(d_model, d_model)

    def forward(self, enc_outputs, memory_key_padding_mask=None):
        attn = self.w_1(enc_outputs)
        attn = self.softmax(attn)
        attn = self.dropout(attn)
        if (memory_key_padding_mask is not None):
            attn = attn.masked_fill(memory_key_padding_mask, float('-inf'))
        attnT = torch.bmm(attn, enc_outputs)
        attnT = self.w_2(attnT)
        return attnT



d_model = 1
func = Model(256).to('cuda')



enc_outputs = torch.randn(2048, 256)




memory_key_padding_mask = torch.randint(2, size=(2048, 256), dtype=torch.int64)


test_inputs = [enc_outputs, memory_key_padding_mask]

# JIT_FAIL
'''
direct:
masked_fill only supports boolean masks, but got dtype Long

jit:
Failed running call_method masked_fill(*(FakeTensor(..., device='cuda:0', size=(2048, 256)), FakeTensor(..., device='cuda:0', size=(2048, 256), dtype=torch.int64), -inf), **{}):
expected predicate to be bool, got torch.int64

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''