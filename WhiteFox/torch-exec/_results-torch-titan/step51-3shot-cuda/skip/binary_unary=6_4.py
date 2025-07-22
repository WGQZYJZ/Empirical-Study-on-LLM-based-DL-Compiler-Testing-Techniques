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
        super().__init()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = (v1 - x2)
        v3 = torch.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.rand(1, 8)


test_inputs = [x1, x2]
