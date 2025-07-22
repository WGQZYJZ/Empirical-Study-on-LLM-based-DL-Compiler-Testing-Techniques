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
        self.inp = torch.randn(3, 3)

    def forward(self, x1, x2):
        v1 = (torch.mm(x1, x2) + self.inp)
        return v1.view(1)




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
shape '[1]' is invalid for input of size 9

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(3, 3)), 1), **{}):
shape '[1]' is invalid for input of size 9

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''