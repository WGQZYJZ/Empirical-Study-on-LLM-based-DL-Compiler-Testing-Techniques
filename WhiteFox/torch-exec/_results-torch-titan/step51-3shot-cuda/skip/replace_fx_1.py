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

    def __init__(self, p2):
        super().__init__()
        self.register_buffer('self.p2', torch.tensor(p2))
        self.bn = torch.nn.BatchNorm1d(2)

    def forward(self, x1):
        x2 = self.bn(x1)
        x3 = torch.rand_like(x2)
        return x3




p2 = 0.7


func = Model(p2).to('cuda')



x1 = torch.randn(3, 3)


test_inputs = [x1]
