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
        self.input_channels = 10
        self.hidden_feature_size = 20
        self.negative_slope = negative_slope
        self.linear1 = torch.nn.Linear(self.input_channels, self.hidden_feature_size)

    def forward(self, x):
        t1 = self.linear1(x)
        t2 = (t1 > 0)
        t3 = (t1 * self.negative_slope)
        t4 = torch.where(condition)
        return t4



negative_slope = 1
func = Model(0.05).to('cuda')



x = torch.randn(1, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'condition' is not defined

jit:
name 'condition' is not defined

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''