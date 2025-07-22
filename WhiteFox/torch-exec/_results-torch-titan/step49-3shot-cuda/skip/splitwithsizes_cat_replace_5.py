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
        super().__init__(features=torch.nn.Sequential(torch.nn.Conv2d(3, 2, kernel_size=(3,))))

    def forward(self, value):
        r = self.features(value)
        return (r, torch.split(value, 2), r)




func = Model().to('cuda')



x1 = torch.rand(1, 3, 32, 32)


test_inputs = [x1]
