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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = torch.nn.functional.softmax(v2, dim=1)[:, 1]
        q = v3.reshape(2, 2).t()
        w = torch.addmm(self.linear.bias, v1, self.linear.weight.t())
        y = torch.nn.functional.sigmoid(w.view(2, 2))
        return (q + y)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[2, 2]' is invalid for input of size 2

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 2)), 2, 2), **{}):
shape '[2, 2]' is invalid for input of size 2

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''