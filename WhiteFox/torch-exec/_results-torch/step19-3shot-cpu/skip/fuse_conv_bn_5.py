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
        self._modules = ['layer']
        s = torch.nn.Sequential(torch.nn.Conv2d(4, 8, 2), torch.nn.BatchNorm2d(8))
        self.layer = s

    def forward(self, x1):
        y = self.layer(x1)
        return y



func = Model().to('cpu')


x1 = torch.randn(1, 4, 4, 4)

test_inputs = [x1]
