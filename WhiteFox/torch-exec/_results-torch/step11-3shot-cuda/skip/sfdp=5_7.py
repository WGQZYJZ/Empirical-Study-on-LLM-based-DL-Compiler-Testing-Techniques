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
        self.fc1 = torch.nn.Linear(...)
        self.fc2 = torch.nn.Linear(...)
        self.fc3 = torch.nn.Linear(...)
        self.fc4 = torch.nn.Linear(...)

    def forward(self, x1, x2, x3, mask):
        v1 = self.fc1(x1)
        v2 = self.fc2(x2)
        v3 = self.fc3(x3)
        v4 = self.fc4(torch.cat((v1, v2, v3), -1))
        v5 = torch.softmax(v4, dim=-1)
        output = v5.masked_fill(mask == 0, float('-inf'))
        return output


func = Model().to('cuda')

x1 = 1
x2 = 1
x3 = 1
mask = 1

test_inputs = [x1, x2, x3, mask]
