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
        self.linear = torch.nn.Linear(2, 2).cuda()
        self.bias = torch.nn.Parameter([0.1, 0.2])

    def forward(self, x1):
        v4 = x1.cuda()
        v1 = torch.nn.functional.linear(v4, self.linear.weight.cuda(), self.linear.bias.cuda())
        v2 = v1.permute(0, 2, 1).cuda()
        v3 = torch.add(v2, self.bias, alpha=0)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]
