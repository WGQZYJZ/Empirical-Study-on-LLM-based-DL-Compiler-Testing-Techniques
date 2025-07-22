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

class Model(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, 5)
        self.fc2 = nn.Linear(5, 3)

    def forward(self, x):
        x = self.fc1(x)
        x = nn.Functional.relu(x)
        x = self.fc2(x)
        x = nn.Functional.relu(x)
        x = nn.Functional.relu(x)
        x = self.fc2(x)
        x = nn.Functional.relu(x)
        x = self.fc2(x)
        x = nn.Functional.relu(x)
        return x


func = Model().to('cpu')


x1 = torch.randn(4, 2)

test_inputs = [x1]
