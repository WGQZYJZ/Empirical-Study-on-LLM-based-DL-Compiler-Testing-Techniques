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

    def __init__(self, n_head, d_value, d_key, d_model, dim_feedforward, dropout_p):
        super().__init__()
        self.self_attn = torch.nn.MultiheadAttention(d_model, n_head, dropout=dropout_p)
        self.linear1 = torch.nn.Linear(d_model, dim_feedforward)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.linear2 = torch.nn.Linear(dim_feedforward, d_model)

    def forward(self, x1):
        (attn_output, _) = self.self_attn(x1, x1, x1)
        v1 = torch.nn.functional.relu(self.linear1(attn_output))
        v2 = self.dropout(v1)
        out = self.linear2(v2)
        return out


n_head = 1
d_value = 1
d_key = 1
d_model = 1
dim_feedforward = 1
dropout_p = 1

func = Model(n_head, d_value, d_key, d_model, dim_feedforward, dropout_p).to('cpu')


x1 = torch.randn(35, 32, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
was expecting embedding dimension of 1, but got 64

jit:
Failed running call_function <function multi_head_attention_forward at 0x721f01005dc0>(*(FakeTensor(..., size=(35, 32, 64)), FakeTensor(..., size=(35, 32, 64)), FakeTensor(..., size=(35, 32, 64)), 1, 1, Parameter(FakeTensor(..., size=(3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), None, None, False, 1, Parameter(FakeTensor(..., size=(1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True))), **{'training': False, 'key_padding_mask': None, 'need_weights': True, 'attn_mask': None, 'average_attn_weights': True, 'is_causal': False}):
was expecting embedding dimension of 1, but got 64

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1373, in forward
    attn_output, attn_output_weights = F.multi_head_attention_forward(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''