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



class Model(module.Module):

    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = module.Linear(in_features=128, out_features=729, bias=True)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3



min_value = 1
max_value = 1
func = Model((- 0.4692587411870063), 0.7854830915257639).to('cuda')



x1 = torch.randn(1, 128)


test_inputs = [x1]
