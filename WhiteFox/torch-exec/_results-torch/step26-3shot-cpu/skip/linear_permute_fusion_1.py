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

class Model(LeNet):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        y = x1
        v1 = torch.nn.functional.linear(y, self.layer4.weight, self.layer4.bias)
        v2 = v1.permute(0, 2, 1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(3, 1, 32, 32)

test_inputs = [x1]
