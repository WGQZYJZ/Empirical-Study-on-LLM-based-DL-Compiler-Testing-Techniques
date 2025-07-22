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

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        return torch.cat([input, v2, v2], 1)




func = Model().to('cuda')



x1 = torch.randn(1, 8)



x2 = torch.randn(8, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got builtin_function_or_method

jit:
expected Tensor as element 0 in argument 0, but got builtin_function_or_method
'''