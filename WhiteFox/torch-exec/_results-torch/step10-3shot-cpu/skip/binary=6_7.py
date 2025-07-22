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

class Model(torch.nn.Module, Exporter):

    def __init__(self, other):
        super().__init__()
        self.linear = Linear(16 * 5 * 5, 10)
        self.other = other

    @Export(method='forward')
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - self.other
        return v2


other = 1
func = Model(1).to('cpu')


x = torch.randn(1, 1, 28, 28)

test_inputs = [x]
