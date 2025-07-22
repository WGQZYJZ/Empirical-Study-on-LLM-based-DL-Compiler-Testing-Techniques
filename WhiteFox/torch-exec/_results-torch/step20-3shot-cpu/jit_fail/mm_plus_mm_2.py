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

class Model(nn.Module):

    def forward(self, input):
        t1 = torch.mm(input)
        t2 = torch.mm(input)
        t3 = torch.mm(torch.cat([t1, t2]))
        t4 = torch.mm(torch.cat([t1, torch.mm(t1, t2)]), t3)
        return torch.mm(t3, t4)



func = Model().to('cpu')


input = torch.randn(55, 55)

test_inputs = [input]

# JIT_FAIL
'''
direct:
mm() missing 1 required positional arguments: "mat2"

jit:
mm() missing 1 required positional arguments: "mat2"
'''