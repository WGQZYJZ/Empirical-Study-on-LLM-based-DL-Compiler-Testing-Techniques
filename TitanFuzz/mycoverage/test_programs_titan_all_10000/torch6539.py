import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 5)
pinv_data = torch.linalg.pinv(input_data)