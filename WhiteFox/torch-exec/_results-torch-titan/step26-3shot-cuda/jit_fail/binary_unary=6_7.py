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

    def forward(self, x):
        x = self.linear(x)
        y = torch.tensor([(- 17.44), 127.27, (- 1.53)])
        x = (x - y)
        x = torch.nn.functional.relu(x)
        return x



func = Model().to('cuda')



x = torch.randn(1, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 3)), FakeTensor(..., size=(3,))), **{}):
Unhandled FakeTensor Device Propagation for aten.sub.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''