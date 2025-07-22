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
        self.layer = torch.nn.Sequential([torch.nn.Conv2d(3, 3, 1, stride=1, padding=1), torch.nn.ReLU(), torch.nn.Dropout2d(0.1)])

    def forward(self, x1):
        v1 = self.layer(x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]
