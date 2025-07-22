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

    def __init__(self, d=512, h=8, dropout=0.0):
        super().__init__()
        self.d = d
        self.h = h
        self.dropout = dropout
        self.linear_layers = nn.ModuleList([nn.Linear(d, d) for _ in range(2)])
        self.norm_layers = nn.ModuleList([nn.LayerNorm(d) for _ in range(3)])

    def attention(self, x):
        y = self.norm_layers[0](x)
        y = self.linear_layers[0](y)
        y = self.linear_layers[1](y).softmax((- 2))
        y = self.norm_layers[1](y)
        output = self.norm_layers[2](x)
        output = (output * y)
        output = output.sum((- 2))
        return output

    def forward(self, x):
        return self.attention(x)



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given normalized_shape=[512], expected input with shape [*, 512], but got input of size[1, 3, 64, 64]

jit:
Failed running call_module sub0_0(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{}):
Given normalized_shape=[512], expected input with shape [512], but got input of size torch.Size([1, 3, 64, 64])

from user code:
   File "<string>", line 36, in forward
  File "<string>", line 26, in attention


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''