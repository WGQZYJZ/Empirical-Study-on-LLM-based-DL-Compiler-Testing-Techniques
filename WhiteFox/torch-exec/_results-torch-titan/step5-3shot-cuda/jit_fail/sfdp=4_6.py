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
        self.key = torch.nn.Linear(8, 8)
        self.query = torch.nn.Linear(8, 8)

    def forward(self, input_tensor, attention_mask):
        attention_mask.data = (attention_mask.data * (- 10000.0))
        q = ((self.query(input_tensor) @ self.key(input_tensor).transpose((- 2), (- 1))) / math.sqrt(self.query(input_tensor).size((- 1))))
        q = (q + attention_mask)
        attn_weight = torch.softmax(q, dim=(- 1))
        output = (attn_weight @ input_tensor)
        return output



func = Model().to('cuda')



input_tensor = torch.randn(64, 8, 56, 56)



attention_mask = attention_mask = torch.randn(64, 1, 56, 56)


test_inputs = [input_tensor, attention_mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (28672x56 and 8x8)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(64, 8, 56, 56)),), **{}):
a and b must have same reduction dim, but got [28672, 56] X [8, 8].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''