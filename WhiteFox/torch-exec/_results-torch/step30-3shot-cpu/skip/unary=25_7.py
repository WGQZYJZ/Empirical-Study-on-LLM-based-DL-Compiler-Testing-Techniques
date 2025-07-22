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
        self.linear = torch.nn.Linear(16, 32, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.linear(x1.flatten(-2))
        v2 = v1 > 0
        v3 = v1 * 0.01
        v4 = torch.where(v2, v1, v3)
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 16)

test_inputs = [x1]
