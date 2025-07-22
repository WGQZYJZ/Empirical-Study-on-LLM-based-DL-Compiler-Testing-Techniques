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
        self.linear = torch.nn.Linear(__SIZE_1__, __SIZE_2__)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - __VALUE___)
        return v2



func = Model().to('cuda')

x1 = 1

test_inputs = [x1]
