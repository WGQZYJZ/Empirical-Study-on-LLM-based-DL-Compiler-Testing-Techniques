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

    def __init__(self, dim_in, dim_hidden):
        super().__init__()
        self.multi_head_attn = torch.nn.MultiheadAttention(dim_in, 8)

    def forward(self, x1, x2, x3):
        v1 = self.multi_head_attn(x1, x2, x3, need_weights=False)
        return v1


dim_in = 1
dim_hidden = 1
func = Model(32, 32).to('cpu')


x1 = torch.randn(1, 8, 32, 32)

x2 = torch.randn(1, 8, 32, 32)

x3 = torch.randn(1, 8, 32, 32)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

jit:
Failed running call_function <function multi_head_attention_forward at 0x7f9634a84dc0>(*(FakeTensor(..., size=(1, 8, 32, 32)), FakeTensor(..., size=(1, 8, 32, 32)), FakeTensor(..., size=(1, 8, 32, 32)), 32, 8, Parameter(FakeTensor(..., size=(96, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(96,), requires_grad=True)), None, None, False, 0.0, Parameter(FakeTensor(..., size=(32, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True))), **{'training': False, 'key_padding_mask': None, 'need_weights': False, 'attn_mask': None, 'average_attn_weights': True, 'is_causal': False}):
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1373, in forward
    attn_output, attn_output_weights = F.multi_head_attention_forward(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''