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

    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.linear(3, 8, bias=False)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        is_positive = v1 > 0
        negative_part = -self.negative_slope * v1
        v2 = torch.where(is_positive, v1, negative_part)
        return v2


negative_slope = 1
func = Model(-1.0).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]
