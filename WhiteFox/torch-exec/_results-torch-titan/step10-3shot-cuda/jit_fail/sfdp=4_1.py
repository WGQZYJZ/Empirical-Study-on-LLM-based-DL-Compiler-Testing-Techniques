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
func = Model(32, 32).to('cuda')



x1 = torch.randn(1, 8, 32, 32)



x2 = torch.randn(1, 8, 32, 32)



x3 = torch.randn(1, 8, 32, 32)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

jit:
Failed running call_module L__self___multi_head_attn(*(FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32))), **{'need_weights': False}):
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''