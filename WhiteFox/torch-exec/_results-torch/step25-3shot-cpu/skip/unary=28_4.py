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

    def __init__(self, min_value=-5, max_value=10):
        super().__init__()
        self.weight = torch.rand(1, 8, dtype=np.float32)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = torch.tensordot(x1, self.weight, dims=1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 16, 3)

test_inputs = [x1]
