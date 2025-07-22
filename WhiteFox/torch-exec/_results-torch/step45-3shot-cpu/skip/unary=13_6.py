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
        super().__init__(5, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.weight, self.bias)
        v2 = torch.sigmoid(v1)
        v3 = v2 * v1
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 5)

test_inputs = [x1]
