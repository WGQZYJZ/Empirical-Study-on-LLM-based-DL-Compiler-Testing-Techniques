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
        self.linear = torch.nn.Linear(features_in, features_out)
        self.leaky_relu_activation = torch.Tensor(negative_slope)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0)
        v3 = (v1 * self.leaky_relu_activation)
        v4 = torch.where(v2, v1, v3)
        return v4



negative_slope = 1
func = Model(0.1).to('cuda')

x1 = 1

test_inputs = [x1]
