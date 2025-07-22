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
        self.permute1 = torch.Tensor.permute

    def forward(self, x1, x2):
        v1 = self.permute1(x1, 0, 2, 1)
        v2 = self.permute1(x2, 0, 2, 1)
        v3 = torch.matmul(v1, v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 3, 3, 3)

x2 = torch.randn(2, 3, 3, 3)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 4 is not equal to len(dims) = 3

jit:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 4 is not equal to len(dims) = 3
'''