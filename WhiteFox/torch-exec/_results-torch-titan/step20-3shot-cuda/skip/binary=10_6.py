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
        self.linear1 = torch.nn.Linear(3, 8, in_features=3, bias=True)
        self.linear2 = torch.nn.Linear(8, 8, in_features=8, bias=True)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = (v1 + other)
        v3 = self.linear2(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 8, 32, 32)


test_inputs = [x1, x2]
