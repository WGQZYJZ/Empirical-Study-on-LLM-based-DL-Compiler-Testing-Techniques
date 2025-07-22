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

class model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            x2 = torch.nn.functional.dropout2d(x1.clone(), p=0.5, inplace=True)
        x3 = torch.randn_like(x2, requires_grad=True)
        return x3



func = model().to('cpu')


x1 = torch.randn(1, 3, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'warnings' is not defined

jit:
NameError: name 'warnings' is not defined

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''