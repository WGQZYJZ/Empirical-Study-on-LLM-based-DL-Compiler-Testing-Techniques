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

class MultiHeadAttention(nn.Module):

    def __init__(self, heads: int, d_model: int, dropout_probability: float):
        super().__init__()
        self.mha = nn.MultiheadAttention(d_model, heads, dropout=dropout_probability, batch_first=True)
        self.drop = nn.Dropout(dropout_probability)
        self.identity = nn.Identity()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.identity(self.mha(x, self.drop(x), self.drop(x))[0])


heads = 1
d_model = 1
dropout_probability = 1

func = MultiHeadAttention(heads, d_model, dropout_probability).to('cpu')


x_ = torch.randn(1, 196, 224)

test_inputs = [x_]

# JIT_FAIL
'''
direct:
was expecting embedding dimension of 1, but got 224

jit:
Failed running call_function <function multi_head_attention_forward at 0x7d7c18a44dc0>(*(FakeTensor(..., size=(196, 1, 224)), FakeTensor(..., size=(196, 1, 224)), FakeTensor(..., size=(196, 1, 224)), 1, 1, Parameter(FakeTensor(..., size=(3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), None, None, False, 1, Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{'training': False, 'key_padding_mask': None, 'need_weights': True, 'attn_mask': None, 'average_attn_weights': True, 'is_causal': False}):
was expecting embedding dimension of 1, but got 224

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1373, in forward
    attn_output, attn_output_weights = F.multi_head_attention_forward(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''