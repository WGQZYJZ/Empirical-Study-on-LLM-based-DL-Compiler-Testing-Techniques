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



class my_view(torch.nn.Module):

    def forward(self, x):
        return x.view(1, 28, 28)




func = my_view().to('cuda')



x = torch.randn(32, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[1, 28, 28]' is invalid for input of size 320

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(32, 10)), 1, 28, 28), **{}):
shape '[1, 28, 28]' is invalid for input of size 320

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''