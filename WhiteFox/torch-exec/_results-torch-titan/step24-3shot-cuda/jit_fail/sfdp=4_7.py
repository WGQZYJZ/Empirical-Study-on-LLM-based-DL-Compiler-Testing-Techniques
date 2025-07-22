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

    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = (embed_dim // num_heads)
        self.proj_query = torch.nn.Linear(embed_dim, embed_dim)
        self.proj_key = torch.nn.Linear(embed_dim, embed_dim)
        self.proj_value = torch.nn.Linear(embed_dim, embed_dim)

    def forward(self, x1):
        q = self.proj_query(x1)
        k = self.proj_key(x1)
        v = self.proj_value(x1)
        q = q.reshape(1, (- 1), self.num_heads, self.head_dim)
        k = k.reshape(1, (- 1), self.num_heads, self.head_dim)
        v = v.reshape(1, (- 1), self.num_heads, self.head_dim)



embed_dim = 1
num_heads = 1

func = Model(embed_dim, num_heads).to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___proj_query(*(1,), **{}):
linear(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''