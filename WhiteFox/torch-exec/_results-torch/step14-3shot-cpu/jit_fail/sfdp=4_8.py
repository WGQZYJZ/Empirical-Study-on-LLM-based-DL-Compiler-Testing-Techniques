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
        self.query = torch.nn.Linear(32, 8)
        self.key = torch.nn.Linear(32, 8)
        self.value = torch.nn.Linear(32, 8)

    def forward(self, x1):
        qk = self.query(x1) @ self.key.T() / math.sqrt(self.query.out_features)
        v1 = qk + 0.5
        v2 = torch.softmax(v1, dim=-1)
        output = v2 @ self.value(x1)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Linear' object has no attribute 'T'

jit:
'Linear' object has no attribute 'T'
'''