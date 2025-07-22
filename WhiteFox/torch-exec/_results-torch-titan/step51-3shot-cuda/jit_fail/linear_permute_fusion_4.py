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
        self.linear = torch.nn.Linear(2, 2, bias=False)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        x2 = torch.zeros(4, 2, 2)
        x3 = x2.permute(0, 2, 1)
        v2 = v1.permute(0, 2, 1)
        x4 = torch.zeros(4, 2, 2)
        v2 = x4.permute(0, 2, 1)
        return torch.nn.functional.linear(x4, torch.tensor([[(- 1.0672), 0.9924], [0.6685, 0.6025]], requires_grad=True), v2)




func = Model().to('cuda')



x1 = torch.randn(4, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
expand(torch.FloatTensor{[4, 2, 2]}, size=[8, 2]): the number of sizes provided (2) must be greater or equal to the number of dimensions in the tensor (3)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(4, 2, 2)), FakeTensor(..., size=(2, 2), requires_grad=True), FakeTensor(..., size=(4, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -2! Mismatching argument at index 1 had torch.Size([4, 2, 2]); but expected shape should be broadcastable to [1, 8, 2]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''