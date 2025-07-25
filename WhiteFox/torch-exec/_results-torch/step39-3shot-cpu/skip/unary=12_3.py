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
        self.in_features = 4 * 8
        self.out_features = 4 * 8
        self.linear = torch.nn.Linear(self.in_features, self.out_features)
        self.conv = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1, bias=True)
        self.conv_weight = torch.randn([8, 8, 1, 1])
        self.conv_bias = torch.randn([8])
        self.conv.weight.copy_(self.conv_weight)
        self.conv.bias.copy_(self.conv_bias)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = F.sigmoid(v1)
        v3 = F.linear(v2, self.linear.weight, self.linear.bias)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 8, 64, 64)

test_inputs = [x1]
