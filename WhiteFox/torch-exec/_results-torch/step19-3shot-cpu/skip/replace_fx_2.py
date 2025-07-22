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
        self.layer1 = torch.nn.Conv2d(3, 32, 5)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.nn.functional.dropout(x, p=0.5)
        return x



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]
