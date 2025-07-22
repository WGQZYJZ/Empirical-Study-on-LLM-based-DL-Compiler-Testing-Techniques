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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = Linear(5, 3)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v0 = self.linear(x1)
        v1 = torch.clamp_min(v0, self.min_value)
        v2 = torch.clamp_max(v1, self.max_value)
        return v2



min_value = 1
max_value = 1
func = Model(0, 1).to('cuda')



x1 = torch.randn(1, 5, 64, 64)


test_inputs = [x1]
