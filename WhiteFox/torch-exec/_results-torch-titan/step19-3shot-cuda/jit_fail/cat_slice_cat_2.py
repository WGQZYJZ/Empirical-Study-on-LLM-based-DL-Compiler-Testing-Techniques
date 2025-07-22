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

    def forward(self, *args):
        lstm = torch.nn.LSTM(input_size=64, hidden_size=64, num_layers=1, batch_first=True)
        (lstm1, _) = lstm(args[0])
        v1 = torch.cat([args[0], lstm1], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:16]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 50, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input and parameter tensors are not at the same device, found input tensor at cuda:0 and parameter tensor at cpu

jit:
Input and parameter tensors are not at the same device, found input tensor at cuda:0 and parameter tensor at cpu
'''