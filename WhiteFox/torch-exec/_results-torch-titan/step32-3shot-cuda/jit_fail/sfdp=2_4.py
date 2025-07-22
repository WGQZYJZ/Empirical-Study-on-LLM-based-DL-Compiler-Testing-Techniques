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

func = MultiHeadAttention(heads, d_model, dropout_probability).to('cuda')



x_ = torch.randn(1, 196, 224)


test_inputs = [x_]

# JIT_FAIL
'''
direct:
was expecting embedding dimension of 1, but got 224

jit:
Failed running call_module L__self___mha(*(FakeTensor(..., device='cuda:0', size=(1, 196, 224)), FakeTensor(..., device='cuda:0', size=(1, 196, 224)), FakeTensor(..., device='cuda:0', size=(1, 196, 224))), **{}):
was expecting embedding dimension of 1, but got 224

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''