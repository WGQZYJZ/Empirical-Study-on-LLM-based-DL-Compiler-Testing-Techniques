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
func = Model(5, 30).to('cuda')



x = torch.randn(1, 5, 30, 40)


test_inputs = [x]

# JIT_FAIL
'''
direct:
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

jit:
Failed running call_module L__self___multi_head(*(FakeTensor(..., device='cuda:0', size=(1, 5, 30, 40)), FakeTensor(..., device='cuda:0', size=(1, 5, 30, 40)), FakeTensor(..., device='cuda:0', size=(1, 5, 30, 40))), **{}):
query should be unbatched 2D or batched 3D tensor but received 4-D query tensor

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''