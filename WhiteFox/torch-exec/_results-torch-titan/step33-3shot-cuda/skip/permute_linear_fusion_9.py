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
        self.linear1 = nn.Linear(in_features=2, out_features=2)
        self.sigmoid = functional.sigmoid
        self.linear = nn.Linear(in_features=1, out_features=2)
        self.clamp = torch.clamp

    def forward(self, x):
        x1 = self.clamp(x, 0.0, 10.0)
        x2 = self.linear1(x1)
        x3 = self.sigmoid(x2)
        x4 = x3.permute(0, 2, 1)
        x5 = functional.linear(x4, weight=self.linear.weight, bias=self.linear.bias)
        return (x2 + x5)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2)


test_inputs = [x1]
