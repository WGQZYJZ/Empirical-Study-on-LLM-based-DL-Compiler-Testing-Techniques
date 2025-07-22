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
        super().__init__(3, 8, kernel_size=3, padding=0, bias=True)

    def forward(self, x):
        v = torch.tanh(super().forward(x))
        return v



func = ModelTanh().to('cpu')


x = torch.randn(4, 3, 512, 1024)

test_inputs = [x]
