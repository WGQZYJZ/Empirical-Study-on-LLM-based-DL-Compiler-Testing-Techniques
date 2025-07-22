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
        self.fc1 = torch.nn.Linear(8, 64)
        self.relu1 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(64, 8)
        self.add1 = torch.nn.Add()

    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = self.relu1(v1)
        v3 = self.fc2(v2)
        v4 = -5.0
        v5 = self.add1(v3, v4)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 8)

test_inputs = [x1]
