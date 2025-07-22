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
        self.fc = torch.nn.Linear(7, 5)
        self.fc2 = torch.nn.Linear(5, 6)

    def forward(self, x1, x2):
        v1 = self.fc(x1)
        v2c = (v1 + x2)
        v3 = torch.relu(v2c)
        return v3




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 4, 1, stride=1, padding=1)
        torch.nn.init.xavier_normal(self.conv.weight)
        self.fc = torch.nn.Linear(32, 1)
        init_weights(self.fc)

    def forward(self, x1):
        v1 = torch.relu(self.conv(x1))
        v2 = v1.view(v1.size(0), (- 1))
        v3 = self.fc(v2).view(v2.size(0), (- 1))
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)



x2 = torch.randn(1, 32)


test_inputs = [x1, x2]
