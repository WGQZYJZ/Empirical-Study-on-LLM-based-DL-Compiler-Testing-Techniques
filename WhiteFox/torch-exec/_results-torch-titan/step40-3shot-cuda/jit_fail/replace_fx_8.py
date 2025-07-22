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

    def __init__(self, a):
        super().__init__()
        self.a = a

    def forward(self, x1):
        x2 = torch.nn.functional.dropout(x1, p=(torch.rand(1) * (1.05 ** self.a)))
        x3 = torch.rand_like(x1)
        return x3



a = 1

func = Model(a).to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
dropout(): argument 'p' (position 2) must be float, not Tensor

jit:
dropout(): argument 'p' (position 2) must be float, not Tensor
'''