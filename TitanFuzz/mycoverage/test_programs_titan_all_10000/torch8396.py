import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randperm(10)
input_data = torch.randperm(10, dtype=torch.float32)