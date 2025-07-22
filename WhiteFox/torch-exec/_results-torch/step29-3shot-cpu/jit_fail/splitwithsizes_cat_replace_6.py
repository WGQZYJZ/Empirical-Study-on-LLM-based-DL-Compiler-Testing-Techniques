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
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.Conv2d(32, 32, 3, 2, 3), torch.nn.Conv2d(32, 32, 3, 1, 1), torch.nn.ReLU(inplace=False)])

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(_forward_relu(split_tensors), dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))

    def _forward_relu(self, split_tensors):
        xs = []
        for x in split_tensors:
            x = torch.sigmoid(x)
            x = torch.tanh(x)
            xs.append(x)
        return xs



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name '_forward_relu' is not defined

jit:
NameError: name '_forward_relu' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''