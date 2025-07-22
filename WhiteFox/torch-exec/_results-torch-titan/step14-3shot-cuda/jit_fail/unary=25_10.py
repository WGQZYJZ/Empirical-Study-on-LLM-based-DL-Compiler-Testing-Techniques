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

    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, X):
        Y = torch.nn.functional.linear(X, self.weight, bias)
        Y_mask = (Y != 0)
        return torch.where(Y_mask, Y, ((- self.negative_slope) * Y))



negative_slope = 1

func = Model(negative_slope).to('cuda')



X = torch.randn(1, 3)


test_inputs = [X]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'weight'

jit:
weight

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''