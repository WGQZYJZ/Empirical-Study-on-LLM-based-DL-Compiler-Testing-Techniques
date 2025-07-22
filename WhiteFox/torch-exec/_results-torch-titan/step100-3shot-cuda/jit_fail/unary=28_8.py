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
        self.fc1 = torch.nn.Linear(64, 64)

    def forward(self, x):
        v1 = self.fc1(x)
        return torch.clamp_min(torch.clamp_max(v1, min), max)



func = Model().to('cuda')



x = torch.randn(1, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
clamp_max() received an invalid combination of arguments - got (Tensor, builtin_function_or_method), but expected one of:
 * (Tensor input, Tensor max, *, Tensor out)
 * (Tensor input, Number max, *, Tensor out)


jit:
clamp_max() received an invalid combination of arguments - got (Tensor, builtin_function_or_method), but expected one of:
 * (Tensor input, Tensor max, *, Tensor out)
 * (Tensor input, Number max, *, Tensor out)

'''