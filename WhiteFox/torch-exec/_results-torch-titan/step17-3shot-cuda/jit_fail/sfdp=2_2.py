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
        self.dropout_p = np.random.uniform(low=0.0, high=0.1)

    def forward(self, __x1__, __x2__, __x3__):
        qk = torch.matmul(__x1__, __x2__.transpose((- 2), (- 1)))




func = Model().to('cuda')

__x1__ = 1
__x2__ = 1
__x3__ = 1

test_inputs = [__x1__, __x2__, __x3__]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''