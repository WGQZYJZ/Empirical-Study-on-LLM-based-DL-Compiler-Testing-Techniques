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

    def __init__(self, lower_bound, upper_bound):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.lower = lower_bound
        self.upper = upper_bound

    def forward(self, x):
        x1 = self.linear(x)
        x2 = torch.clamp_min(x1, self.lower)
        x3 = torch.clamp_max(x2, self.upper)
        return x3



lower_bound = 1
upper_bound = 1
func = Model(lb, ub).to('cuda')



x3 = torch.randn(1, 3)


test_inputs = [x3]
