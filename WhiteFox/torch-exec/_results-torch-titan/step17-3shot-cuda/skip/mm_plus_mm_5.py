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



class Net(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 20, 5, 1)
        self.conv2 = torch.nn.Conv2d(20, 50, 5, 1)
        z = torch.randn(4, 4)
        z2 = torch.randn(1, 4, 4, 4)
        self.conv2(self.conv1(z.view(1, 1, 4, 4)))
        self.conv2(self.conv1(z2))




func = Net().to('cuda')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]
