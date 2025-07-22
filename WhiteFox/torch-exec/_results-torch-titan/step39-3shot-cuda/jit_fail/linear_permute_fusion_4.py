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
        v4 = (v1 * 1)
        v2 = self.block(v1, src_key_padding_mask=(v4 == 0))
        v3 = (v2 * 1)
        return v3




func = Model().to('cuda')



x1 = torch.randn(2, 3, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
For batched (3-D) `query`, expected `key_padding_mask` to be `None` or 2-D but found 3-D tensor instead

jit:
Failed running call_module L__self___block(*(FakeTensor(..., device='cuda:0', size=(3, 2, 2)),), **{'src_key_padding_mask': FakeTensor(..., device='cuda:0', size=(3, 2, 2), dtype=torch.bool)}):
For batched (3-D) `query`, expected `key_padding_mask` to be `None` or 2-D but found 3-D tensor instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''