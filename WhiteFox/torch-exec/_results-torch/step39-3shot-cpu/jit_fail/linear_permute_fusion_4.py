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
        self.block = torch.nn.TransformerEncoderLayer(2, 2)
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        self.block.self_attn.softmax_temp = 1
        v1 = x1.permute(1, 0, 2)
        v4 = v1 * 1
        v2 = self.block(v1, src_key_padding_mask=v4 == 0)
        v3 = v2 * 1
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 3, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
For batched (3-D) `query`, expected `key_padding_mask` to be `None` or 2-D but found 3-D tensor instead

jit:
Failed running call_function <function multi_head_attention_forward at 0x758dd9a9bdc0>(*(FakeTensor(..., size=(3, 2, 2)), FakeTensor(..., size=(3, 2, 2)), FakeTensor(..., size=(3, 2, 2)), 2, 2, Parameter(FakeTensor(..., size=(6, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), None, None, False, 0.1, Parameter(FakeTensor(..., size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{'training': False, 'key_padding_mask': FakeTensor(..., size=(3, 2, 2)), 'need_weights': False, 'attn_mask': None, 'average_attn_weights': True, 'is_causal': False}):
For batched (3-D) `query`, expected `key_padding_mask` to be `None` or 2-D but found 3-D tensor instead

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/transformer.py", line 920, in forward
    + self._sa_block(x, src_mask, src_key_padding_mask, is_causal=is_causal)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/transformer.py", line 934, in _sa_block
    x = self.self_attn(
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1373, in forward
    attn_output, attn_output_weights = F.multi_head_attention_forward(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''