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

    def forward(self, input1, input2, scale, dp):
        v1 = torch.matmul(input1, input2.transpose(-2, -1))
        v2 = v1.mul(scale)
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dp)
        v5 = v4.matmul(input2)
        return v5


func = Model().to('cpu')


input1 = torch.randn(4, 8, 5)

input2 = torch.randn(4, 7, 8)

scale = torch.tensor([1.0])
dp = 1

test_inputs = [input1, input2, scale, dp]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 5] but got: [4, 8].

jit:
Failed running call_function <built-in method matmul of type object at 0x78fc07f96ec0>(*(FakeTensor(..., size=(4, 8, 5)), FakeTensor(..., size=(4, 8, 7))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 5] but got: [4, 8].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''