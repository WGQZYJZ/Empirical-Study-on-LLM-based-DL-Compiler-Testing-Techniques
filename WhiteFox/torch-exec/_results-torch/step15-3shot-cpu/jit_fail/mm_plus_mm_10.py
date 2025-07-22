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

    def forward(self, t1, t2, t3, t4):
        v1 = torch.mm(t1, t3)
        v2 = torch.mm(t3, t2)
        v3 = torch.mm(t1, t4)
        v4 = torch.mm(t4, t2)
        v5 = torch.mm(t3, t4)
        v6 = torch.mm(input1, t3)
        v7 = torch.mm(input2, t4)
        v8 = torch.mm(input1, t1)
        v9 = torch.mm(input2, t2)
        return t3



func = Model().to('cpu')


input1 = torch.randn(33, 33)

input2 = torch.randn(33, 33)

input1 = torch.randn(33, 33)
input1 = torch.randn(33, 33)
t1 = torch.mm(input1, input1)

input1 = torch.randn(33, 33)
input1 = torch.randn(33, 33)
t2 = torch.mm(input1, input1)

t1 = torch.mm(input1, input1)
input1 = torch.randn(33, 33)
t3 = torch.mm(input1, t1)

t1 = torch.mm(input1, input1)
input2 = torch.randn(33, 33)
t4 = torch.mm(input2, t1)

test_inputs = [input1, input2, t1, t2, t3, t4]

# JIT_FAIL
'''
direct:
forward() takes 5 positional arguments but 7 were given

jit:
forward() takes 5 positional arguments but 7 were given
'''