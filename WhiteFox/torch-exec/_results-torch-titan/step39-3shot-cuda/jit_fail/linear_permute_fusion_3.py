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
        conv1 = torch.nn.ConvTranspose2d(2, 2, 2)
        v1 = conv1(x1)
        v2 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 3)), Parameter(FakeTensor(..., device='cuda:0', size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 3] X [2, 2].

from user code:
   File "<string>", line 24, in <resume in forward>


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''