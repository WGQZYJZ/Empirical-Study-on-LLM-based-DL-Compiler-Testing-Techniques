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
        self.matmul5 = torch.matmul
        self.div3 = torch.div
        self.softmax5 = torch.nn.Softmax(dim=-1)
        self.dropout7 = torch.nn.Dropout()
        self.matmul10 = torch.matmul

    def forward(self, input1, input2, input3, input4):
        v0 = self.dropout7(self.softmax5(self.div3(self.matmul5(input1, input2.transpose(-2, -1)), input3)))
        v1 = self.matmul10(v0, input4)
        return v1


func = Model().to('cpu')


input1 = torch.randn(128, 64, 16)

input2 = torch.randn(128, 64, 16)


input3 = torch.arange(16, dtype=torch.float32).unsqueeze(1).repeat(1, 16)

input4 = torch.randn(128, 64, 16)

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (16) at non-singleton dimension 2

jit:
Failed running call_function <built-in method div of type object at 0x70894a596ec0>(*(FakeTensor(..., size=(128, 64, 64)), FakeTensor(..., size=(16, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([16, 16]); but expected shape should be broadcastable to [128, 64, 64]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''