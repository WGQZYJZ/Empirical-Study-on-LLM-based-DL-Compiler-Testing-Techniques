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
        super().__init__(weight=torch.eye(3), bias=torch.ones(3))

    def forward(self, x):
        v1 = F.linear(x.t(), self.weight, self.bias)
        v2 = F.sigmoid(v1)
        v3 = (v1 * v2)
        return v3



func = Model().to('cuda')



x = torch.randn(20, 3)


test_inputs = [x]
