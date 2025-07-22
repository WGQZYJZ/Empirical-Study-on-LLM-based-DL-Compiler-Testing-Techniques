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
        self.layer2 = nn.Linear(10, 10)

    def forward(self, x1):
        v1 = self.layer2(x1)
        v2 = v1 * torch.clamp(torch.min(torch.max(v1 + 3, 0), 6), min=0, max=6)
        v3 = v2 / 6
        return v3


func = Model().to('cpu')


x1 = torch.randn(3, 10)

test_inputs = [x1]
