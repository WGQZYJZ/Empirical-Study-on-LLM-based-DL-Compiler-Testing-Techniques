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

    def __init__(self, num_heads, embed_dim):
        super().__init__()
        self.multi_head = torch.nn.MultiheadAttention(embed_dim, num_heads)

    def forward(self, x):
        (output, _) = self.multi_head(x, x, x)
        return output


num_heads = 1
embed_dim = 1
func = Model(5, 30).to('cpu')


x = torch.randn(1, 5, 30, 40)

test_inputs = [x]

# JIT_FAIL
'''
direct:
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

jit:
Failed running call_function <function multi_head_attention_forward at 0x7203737dbdc0>(*(FakeTensor(..., size=(1, 5, 30, 40)), FakeTensor(..., size=(1, 5, 30, 40)), FakeTensor(..., size=(1, 5, 30, 40)), 30, 5, Parameter(FakeTensor(..., size=(90, 30), requires_grad=True)), Parameter(FakeTensor(..., size=(90,), requires_grad=True)), None, None, False, 0.0, Parameter(FakeTensor(..., size=(30, 30), requires_grad=True)), Parameter(FakeTensor(..., size=(30,), requires_grad=True))), **{'training': False, 'key_padding_mask': None, 'need_weights': True, 'attn_mask': None, 'average_attn_weights': True, 'is_causal': False}):
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1373, in forward
    attn_output, attn_output_weights = F.multi_head_attention_forward(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''