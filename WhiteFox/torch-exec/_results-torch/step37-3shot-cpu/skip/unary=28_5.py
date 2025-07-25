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

class Model_L1_L2(torch.nn.Module):

    def __init__(self, min_value=-1, max_value=1):
        super().__init__()
        if min_value >= max_value:
            raise ValueError('Minimum value must be less than maximum value')
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = torch.flatten(x1, start_dim=1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3.view(x1.size())


func = Model_L1_L2(__min_value__, __max_value__).to('cpu')


x1 = torch.randn(1, 2, 16, 16)

test_inputs = [x1]
