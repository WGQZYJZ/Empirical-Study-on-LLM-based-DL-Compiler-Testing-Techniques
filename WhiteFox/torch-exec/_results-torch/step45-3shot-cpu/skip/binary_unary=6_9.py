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
        self.linear = torch.nn.init.normal_(torch.nn.Linear(14, 10, bias=True))
        self.bias = torch.nn.init.normal_(torch.nn.Parameter(torch.empty(10)))

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 - x2
        v3 = torch.nn.functional.relu(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 14)

x2 = torch.randn(10)

test_inputs = [x1, x2]
