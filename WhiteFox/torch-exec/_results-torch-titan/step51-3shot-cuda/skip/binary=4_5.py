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

    def __init__(self, a, b):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        self.other = torch.nn.Parameter(torch.load(b), requires_grad=False)
        self.bias = torch.nn.Parameter(torch.load(b), requires_grad=False)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.other)
        v3 = (v2 + self.bias)
        return v3



a = 1
b = 1

func = Model(a, b).to('cuda')



x1 = torch.arange(1, 2).reshape([1, 1])


test_inputs = [x1]
