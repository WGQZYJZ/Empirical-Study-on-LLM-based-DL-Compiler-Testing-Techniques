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

    def forward(self, x1):
        attention_mask = generate_attention_mask(x1, x1)
        k1 = torch.exp(torch.randn(x1.shape[1], x1.shape[1]))
        q1 = torch.exp(torch.randn(x1.shape[1], x1.shape[1]))
        v1 = torch.exp(torch.randn(x1.shape[1], x1.shape[1]))
        out = torch.matmul(q1, k1) / math.sqrt(q1.shape[1])
        out *= attention_mask
        attn_weight = torch.softmax(out, dim=1)
        x2 = torch.bmm(attn_weight, v1)
        return x2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'generate_attention_mask' is not defined

jit:
NameError: name 'generate_attention_mask' is not defined

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''