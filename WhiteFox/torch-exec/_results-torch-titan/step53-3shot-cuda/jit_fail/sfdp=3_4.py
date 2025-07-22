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

    def __init__(self, input_dim, num_heads=4, dropout_p=0.5, head_dim=None, scale_factor=math.sqrt(0.5)):
        super().__init__()
        if (head_dim is None):
            head_dim = (input_dim // num_heads)
        self.qk = torch.nn.Linear(input_dim, input_dim)
        self.value = torch.nn.Linear(input_dim, input_dim)
        self.dropout = torch.nn.Dropout(dropout_p)
        self.scale_factor = scale_factor

    def forward(self, x):
        qk = self.qk(x)
        v = self.value(x)
        attn = torch.matmul(qk, v.transpose((- 2), (- 1)))
        scale_attn = attn.mul(self.scale_factor)
        softmax_attn = scale_attn.softmax(dim=(- 1))
        dropout_attn = self.dropout(softmax_attn)
        output = torch.matmul(dropout_attn, v)
        return output



input_dim = 1

func = Model(input_dim).to('cuda')



x = torch.randn(1, 64, 20)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x20 and 1x1)

jit:
Failed running call_module L__self___qk(*(FakeTensor(..., device='cuda:0', size=(1, 64, 20)),), **{}):
a and b must have same reduction dim, but got [64, 20] X [1, 1].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''