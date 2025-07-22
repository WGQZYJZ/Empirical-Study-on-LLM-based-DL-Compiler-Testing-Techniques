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
        self.f = torch.nn.utils.prune.PruningContainer()
        self.f.i = torch.nn.Linear(1, 1)
        self.f.i2 = torch.nn.Linear(1, 1)

    def forward(self, x1, x2, x3):
        v1 = self.f.i(x1)
        v2 = self.f.i2(x2)
        v3 = v1 - x3
        v4 = v2 - v3
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 1)

x2 = torch.randn(1, 1)

x3 = torch.randn(1, 1)

test_inputs = [x1, x2, x3]
