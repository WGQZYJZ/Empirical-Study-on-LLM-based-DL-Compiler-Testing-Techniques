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

class MultiheadAttentionIdentity(torch.nn.MultiheadAttention):

    def forward(self, query, key, value, attn_mask=None):
        return super().forward(query, key, value, attn_mask)

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.attn = MultiheadAttentionIdentity(32, 8)

    def forward(self, x1, x2):
        v1 = self.attn(x1, x2, x2)
        return v1


func = Model().to('cpu')


x1 = torch.randn(128, 32, 64)

x2 = torch.randn(128, 32, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
was expecting embedding dimension of 32, but got 64

jit:
Failed running call_function <function multi_head_attention_forward at 0x798e068c4dc0>(*(FakeTensor(..., size=(128, 32, 64)), FakeTensor(..., size=(128, 32, 64)), FakeTensor(..., size=(128, 32, 64)), 32, 8, Parameter(FakeTensor(..., size=(96, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(96,), requires_grad=True)), None, None, False, 0.0, Parameter(FakeTensor(..., size=(32, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True))), **{'training': False, 'key_padding_mask': None, 'need_weights': True, 'attn_mask': None, 'average_attn_weights': True, 'is_causal': False}):
was expecting embedding dimension of 32, but got 64

from user code:
   File "<string>", line 25, in forward
  File "<string>", line 16, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1373, in forward
    attn_output, attn_output_weights = F.multi_head_attention_forward(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''