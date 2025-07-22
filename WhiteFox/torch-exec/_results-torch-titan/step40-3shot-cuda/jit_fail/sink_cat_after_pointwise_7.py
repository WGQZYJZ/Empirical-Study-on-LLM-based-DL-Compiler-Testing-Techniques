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
        y = torch.cat([].append(x).append(x), dim=1)
        return y.view(y.shape[0], (- 1)).tanh()




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'NoneType' object has no attribute 'append'

jit:
'NoneType' object has no attribute 'append'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''