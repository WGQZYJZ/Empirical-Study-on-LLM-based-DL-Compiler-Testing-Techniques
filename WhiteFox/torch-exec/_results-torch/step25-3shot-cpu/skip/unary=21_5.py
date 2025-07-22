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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(3, 20, 1, stride=1, padding=1, stride=1)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        x = self.conv2d(x)
        x = self.tanh(x)
        return x



func = ModelTanh().to('cpu')


x = torch.randn(128, 3, 224, 224)

test_inputs = [x]
