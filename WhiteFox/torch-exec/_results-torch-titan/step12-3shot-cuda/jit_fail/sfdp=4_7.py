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




func = Model().to('cuda')



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
Failed running call_module L__self___attn(*(FakeTensor(..., device='cuda:0', size=(2, 20, 32)), FakeTensor(..., device='cuda:0', size=(2, 10, 32)), FakeTensor(..., device='cuda:0', size=(2, 10, 32)), FakeTensor(..., device='cuda:0', size=(2, 20, 10), dtype=torch.bool)), **{}):
For batched (3-D) `query`, expected `key_padding_mask` to be `None` or 2-D but found 3-D tensor instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''