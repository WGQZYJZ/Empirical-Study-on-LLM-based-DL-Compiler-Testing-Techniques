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
        self.maxpool = torch.nn.MaxPool2d(3, 2, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.maxpool(x1)
        v2 = (v1 - 100)
        v3 = F.relu(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]
