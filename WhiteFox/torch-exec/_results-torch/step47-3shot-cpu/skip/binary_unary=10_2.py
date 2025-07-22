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
        self.features = torch.nn.Sequential([torch.nn.Linear(256, 64), torch.nn.ReLU()])

    def forward(self, x1):
        v1 = self.features(x1)
        return v1


func = Model().to('cpu')


x1 = torch.randn(1, 256)

test_inputs = [x1]
