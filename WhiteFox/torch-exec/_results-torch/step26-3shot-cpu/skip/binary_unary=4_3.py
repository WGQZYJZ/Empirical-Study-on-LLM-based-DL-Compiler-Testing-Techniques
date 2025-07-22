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

class Model:

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other = other

    def forward(self, x3):
        v1 = self.linear(x3)
        v2 = v1 + self.other
        v3 = torch.relu(v2)
        return v3


other = torch.ones(8)

func = Model(other).to('cpu')


other = torch.ones(8)

x3 = torch.randn(3, 3)

test_inputs = [other, x3]
