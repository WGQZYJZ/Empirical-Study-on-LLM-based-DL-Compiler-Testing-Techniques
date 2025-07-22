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
        self.attn = torch.nn.MultiheadAttention(embed_dim=8, num_heads=2, dropout=0.2)

    def forward(self, x1):
        (output, attention) = self.attn(x1, x1, x1, attn_mask=None, key_padding_mask=None)[0]
        return output



func = Model().to('cuda')



x1 = torch.randn(27, 8, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
was expecting embedding dimension of 8, but got 64

jit:
Failed running call_module L__self___attn(*(FakeTensor(..., device='cuda:0', size=(27, 8, 64)), FakeTensor(..., device='cuda:0', size=(27, 8, 64)), FakeTensor(..., device='cuda:0', size=(27, 8, 64))), **{'attn_mask': None, 'key_padding_mask': None}):
was expecting embedding dimension of 8, but got 64

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''