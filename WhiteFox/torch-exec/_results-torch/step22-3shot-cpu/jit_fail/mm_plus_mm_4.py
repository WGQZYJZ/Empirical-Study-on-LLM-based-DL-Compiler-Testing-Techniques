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
        self.t1 = torch.randn(5, 5)
        self.t2 = torch.randn(5, 5)

    def forward(self, input1, input2):
        t1 = input1.mm(input2.mm(self.t1))
        mmm = t1.mm(self.t1)
        mm = input2.mm(input1.mm(self.t1.mm(self.t2)))
        return t1 + mmm - mm



func = Model().to('cpu')


input1 = torch.randn(8, 8)
input2 = 1

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'mm'

jit:
AttributeError: 'int' object has no attribute 'mm'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''