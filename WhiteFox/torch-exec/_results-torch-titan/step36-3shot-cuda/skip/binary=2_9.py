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
        super(Model, self).__init__()
        self.conv = torch.nn.Conv2d(3, 6, padding=4)

    def forward(self, x):
        x = torch.relu(x)
        x = self.conv(x)
        x = (x - 3.0)
        return x




func = Model().to('cuda')



input_tensor = torch.randn(1, 3, 64, 64)


test_inputs = [input_tensor]
