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

    def __init__(self, other):
        super().__init__()
        __placeholder__

    def forward(self, x1):
        v1 = __self__.linear(x1)
        v2 = v1 - __other__
        v3 = torch.relu(v2)
        return v3


other = 1
func = Model(3).to('cpu')


x1 = torch.randn(1, 64)

test_inputs = [x1]
