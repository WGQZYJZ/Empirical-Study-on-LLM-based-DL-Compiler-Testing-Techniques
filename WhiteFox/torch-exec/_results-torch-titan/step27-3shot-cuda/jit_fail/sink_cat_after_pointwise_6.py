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

    def forward(self, x):
        y1 = (x * 2)
        y2 = (y1 + 3)
        y3 = torch.cat((y1, y2, y1), dim=1)
        y3 = y3.view(y3.shape[:(- 1)])
        y3 = y3.tanh()
        return (y3 + x)




func = Model().to('cuda')



x = torch.randn(5, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[5, 9]' is invalid for input of size 180

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(5, 9, 4)), (5, 9)), **{}):
shape '[5, 9]' is invalid for input of size 180

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''