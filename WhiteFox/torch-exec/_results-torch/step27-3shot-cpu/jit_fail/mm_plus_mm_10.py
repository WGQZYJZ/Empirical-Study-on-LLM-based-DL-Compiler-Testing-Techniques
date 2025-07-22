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

class TorchModel(nn.Module):

    def __init__(self):
        super(TorchModel, self).__init__()

    def forward(self, input):
        v = torch.unsqueeze(input, 2)
        return v.sum(1)



func = TorchModel().to('cpu')


input1 = torch.randn(3, 4)

input2 = torch.randn(3, 4)

input3 = torch.randn(3, 4)

input4 = torch.randn(3, 4)

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''