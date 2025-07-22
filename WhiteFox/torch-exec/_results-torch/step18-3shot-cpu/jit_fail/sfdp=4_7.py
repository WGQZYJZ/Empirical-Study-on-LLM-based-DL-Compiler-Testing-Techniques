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

    def __init__(self, d_model, nhead, num_encoder_layers=1):
        super().__init__()
        encoder_layer = torch.nn.TransformerEncoderLayer(d_model, nhead)
        self.transformer_encoder = torch.nn.TransformerEncoder(encoder_layer, num_encoder_layers)

    def forward(self, src, src_mask=None):
        output = self.transformer_encoder(src, src_mask)
        return output


d_model = 1
nhead = 1

func = Model(d_model, nhead).to('cpu')


src = torch.randn(10, 64, 128)

src_mask = torch.randn(10, 1, 64, 64).round()

test_inputs = [src, src_mask]

# JIT_FAIL
'''
direct:
For batched (3-D) `query`, expected `attn_mask` to be `None`, 2-D or 3-D but found 4-D tensor instead

jit:
Failed running call_function <function multi_head_attention_forward at 0x7d9567a84dc0>(*(FakeTensor(..., size=(10, 64, 128)), FakeTensor(..., size=(10, 64, 128)), FakeTensor(..., size=(10, 64, 128)), 1, 1, Parameter(FakeTensor(..., size=(3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), None, None, False, 0.1, Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{'training': False, 'key_padding_mask': None, 'need_weights': False, 'attn_mask': FakeTensor(..., size=(10, 1, 64, 64)), 'average_attn_weights': True, 'is_causal': False}):
For batched (3-D) `query`, expected `attn_mask` to be `None`, 2-D or 3-D but found 4-D tensor instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/transformer.py", line 517, in forward
    output = mod(
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