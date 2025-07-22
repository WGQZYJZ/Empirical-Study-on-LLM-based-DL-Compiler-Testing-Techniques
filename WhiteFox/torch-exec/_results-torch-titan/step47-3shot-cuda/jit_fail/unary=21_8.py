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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 20)

    def forward(self, x):
        t1 = self.linear(x)
        t2 = torch.tanh(t1)
        return t2.view(20, 5, 5)




func = ModelTanh().to('cuda')



x = torch.randn(80, 50)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[20, 5, 5]' is invalid for input of size 1600

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(80, 20)), 20, 5, 5), **{}):
shape '[20, 5, 5]' is invalid for input of size 1600

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''