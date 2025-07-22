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
        self.attn = torch.nn.MultiheadAttention(64, 4)

    def forward(self, x1, x2):
        (x3, x4) = self.attn(x1, x2, x2)
        return x3


func = Model().to('cuda')


x1 = torch.randn(1, 64, 4, 28)

x2 = torch.randn(1, 64, 28, 28)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

jit:
Failed running call_function <function multi_head_attention_forward at 0x743ce3d44dc0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 4, 28)), FakeTensor(..., device='cuda:0', size=(1, 64, 28, 28)), FakeTensor(..., device='cuda:0', size=(1, 64, 28, 28)), 64, 4, Parameter(FakeTensor(..., device='cuda:0', size=(192, 64), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(192,), requires_grad=True)), None, None, False, 0.0, Parameter(FakeTensor(..., device='cuda:0', size=(64, 64), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(64,), requires_grad=True))), **{'training': False, 'key_padding_mask': None, 'need_weights': True, 'attn_mask': None, 'average_attn_weights': True, 'is_causal': False}):
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1373, in forward
    attn_output, attn_output_weights = F.multi_head_attention_forward(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''