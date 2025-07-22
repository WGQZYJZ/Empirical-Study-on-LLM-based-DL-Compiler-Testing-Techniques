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

    def forward(self, x1, x2, x3):
        t1 = torch.mm(x1 + x2, x1 + x2 + x3)
        t2 = torch.mm(x1, x2)
        t3 = torch.mm(t1, t2)
        return t3



func = Model().to('cuda')

x1 = 1
x2 = 1
x3 = 1

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mm(): argument 'input' (position 1) must be Tensor, not int

jit:
mm(): argument 'input' (position 1) must be Tensor, not int
'''