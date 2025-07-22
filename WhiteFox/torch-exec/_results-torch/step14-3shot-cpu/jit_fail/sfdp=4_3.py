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

    def forward(self, input1, input2):
        q = input1
        k = input2
        v = torch.randn(1, 3, 3, 3)
        qk = torch.matmul(q, k.transpose(-2, -1))
        mask = torch.randint(0, 1, size=(1, 3))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = torch.matmul(torch.matmul(v, attn_weight), -1)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 3, 3, 3)

x2 = torch.randn(1, 3, 6, 6)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 3] but got: [3, 6].

jit:
Failed running call_function <built-in method matmul of type object at 0x77f778d96ec0>(*(FakeTensor(..., size=(1, 3, 3, 3)), FakeTensor(..., size=(1, 3, 6, 6))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 3] but got: [3, 6].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''