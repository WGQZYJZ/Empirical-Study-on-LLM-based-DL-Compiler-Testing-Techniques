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

class ModelTanh(nn.Module):

    def forward(self, x):
        v = nn.Tanh()(x)
        return v[:, :, :, :]



func = ModelTanh().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
tanh(): argument 'input' (position 1) must be Tensor, not int

jit:
tanh(): argument 'input' (position 1) must be Tensor, not int
'''