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
        self.softmax = torch.nn.Softmax()
        self.linear1 = torch.nn.Linear(6400, 16777216)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = x1[0]
        v2 = self.softmax(v1)
        v3 = self.linear1(v2)
        v4 = self.relu(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 6400)

test_inputs = [x1]
