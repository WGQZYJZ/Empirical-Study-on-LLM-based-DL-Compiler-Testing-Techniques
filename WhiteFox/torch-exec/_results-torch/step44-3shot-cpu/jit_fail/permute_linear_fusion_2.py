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
        self.linear = torch.nn.Linear(2, 3)
        self.softmax = torch.nn.Softmax(dim=1)
        self.activation = torch.nn.Tanh()

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = self.softmax(v2)
        v4 = v3.unsqueeze(1)
        v5 = torch.nn.functional.linear(v4, self.linear.weight.transpose(-2, -1), self.linear.bias)
        v6 = v4 + v5
        v7 = self.activation(v6)
        v8 = v7.squeeze(1)
        v9 = v1 * v8
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The expanded size of the tensor (2) must match the existing size (3) at non-singleton dimension 1.  Target sizes: [2, 2].  Tensor sizes: [3]

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 1, 2, 3)), FakeTensor(..., size=(2, 3), requires_grad=True), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([3]); but expected shape should be broadcastable to [2, 2]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''