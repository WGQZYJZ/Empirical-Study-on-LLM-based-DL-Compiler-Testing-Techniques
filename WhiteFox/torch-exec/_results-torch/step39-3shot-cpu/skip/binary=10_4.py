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
        super().__init__(nn.Linear(10, 24), lambda x: x + torch.tensor([0.98]))


func = Model().to('cpu')


x = torch.randn(1, 10)

test_inputs = [x]
