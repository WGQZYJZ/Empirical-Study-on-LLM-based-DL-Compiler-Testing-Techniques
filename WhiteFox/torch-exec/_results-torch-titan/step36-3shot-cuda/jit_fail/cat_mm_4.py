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

    def forward(self, x1):
        v = torch.mm(x1, x1)
        if v:
            return [v, v]
        return [v]




func = Model().to('cuda')



x1 = torch.randn(5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
Boolean value of Tensor with more than one value is ambiguous
'''