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
        self.attn = torch.nn.MultiheadAttention(32, 4, dropout=0.25, batch_first=True)

    def forward(self, tensor1):
        v1 = self.attn(tensor1)
        return v1


func = Model().to('cpu')


tensor1 = torch.randn(1, 4, 32, 32)

test_inputs = [tensor1]

# JIT_FAIL
'''
direct:
forward() missing 2 required positional arguments: 'key' and 'value'

jit:
forward() missing 2 required positional arguments: 'key' and 'value'
'''