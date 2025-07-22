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
        self.matmul1 = torch.nn.Linear(128, 8)
        self.matmul2 = torch.nn.Linear(128, 8)

    def forward(self, inp1, inp2, inp3):
        qk1 = self.matmul1(inp1).reshape(56, 4, 32)
        qk2 = self.matmul2(inp2).reshape(56, 32, 4)
        qk = torch.matmul(qk1, qk2.transpose((- 2), (- 1)))
        scale_factor = (1.0 / np.sqrt(np.shape(inp1)[(- 1)]))
        scaled_qk = (scale_factor * qk)
        attn_weights = torch.softmax(scaled_qk, dim=(- 1))
        dropout_attn_weights = torch.nn.functional.dropout(attn_weights, p=0.5)
        out = torch.matmul(dropout_attn_weights, inp3)
        return out



func = Model().to('cuda')



inp1 = torch.randn(56, 128)



inp2 = torch.randn(56, 4, 32)



inp3 = torch.randn(56, 32, 4)


test_inputs = [inp1, inp2, inp3]

# JIT_FAIL
'''
direct:
shape '[56, 4, 32]' is invalid for input of size 448

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(56, 8)), 56, 4, 32), **{}):
shape '[56, 4, 32]' is invalid for input of size 448

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''