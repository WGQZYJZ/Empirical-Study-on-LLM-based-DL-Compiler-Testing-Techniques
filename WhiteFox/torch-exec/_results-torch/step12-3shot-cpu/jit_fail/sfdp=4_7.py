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
        self.attn = torch.nn.MultiheadAttention(32, 4)

    def forward(self, q1, k1, v1, mask=None):
        o1 = self.attn(q1, k1, v1, mask)
        return o1[0]



func = Model().to('cpu')


q1 = torch.randn(2, 20, 32)

k1 = torch.randn(2, 10, 32)

v1 = torch.randn(2, 10, 32)


mask = torch.randn(2, 20, 10).to(torch.bool)

test_inputs = [q1, k1, v1, mask]

# JIT_FAIL
'''
direct:
For batched (3-D) `query`, expected `key_padding_mask` to be `None` or 2-D but found 3-D tensor instead

jit:
Failed running call_function <function multi_head_attention_forward at 0x77a151b82dc0>(*(FakeTensor(..., size=(2, 20, 32)), FakeTensor(..., size=(2, 10, 32)), FakeTensor(..., size=(2, 10, 32)), 32, 4, Parameter(FakeTensor(..., size=(96, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(96,), requires_grad=True)), None, None, False, 0.0, Parameter(FakeTensor(..., size=(32, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True))), **{'training': False, 'key_padding_mask': FakeTensor(..., size=(2, 20, 10)), 'need_weights': True, 'attn_mask': None, 'average_attn_weights': True, 'is_causal': False}):
For batched (3-D) `query`, expected `key_padding_mask` to be `None` or 2-D but found 3-D tensor instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1373, in forward
    attn_output, attn_output_weights = F.multi_head_attention_forward(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''