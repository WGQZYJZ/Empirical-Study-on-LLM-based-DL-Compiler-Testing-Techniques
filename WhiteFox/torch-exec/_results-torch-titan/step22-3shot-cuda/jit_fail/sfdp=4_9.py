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

    def forward(self, query, key, value, attention_mask):
        qk = (torch.matmul(query, key.transpose((- 2), (- 1))) / math.sqrt(query.size((- 1))))
        qk = (qk + attention_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = torch.matmul(attn_weight, value)
        return output



func = Model().to('cuda')



query = torch.randn(3, 5)



key = torch.randn(4, 5)



value = torch.randn(5, 7)



attention_mask = torch.zeros((3, 4))


test_inputs = [query, key, value, attention_mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x4 and 5x7)

jit:
Failed running call_function <built-in method matmul of type object at 0x7a33c04699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 4)), FakeTensor(..., device='cuda:0', size=(5, 7))), **{}):
a and b must have same reduction dim, but got [3, 4] X [5, 7].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''