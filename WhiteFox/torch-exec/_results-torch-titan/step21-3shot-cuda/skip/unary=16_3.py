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

    def __init__(self, size1, size2):
        super().__init__()
        self.linear = torch.nn.Linear(size1, size2)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.relu(v1)
        return v2



size1 = 1
size2 = 1
func = Model(__size1__, __size2__).to('cuda')



__size1__ = 64


x1 = torch.randn(1, __size1__)


test_inputs = [x1]
