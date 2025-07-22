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
        super().init()
        self.linear = torch.nn.Linear(64, 32)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 64)


test_inputs = [x1]
