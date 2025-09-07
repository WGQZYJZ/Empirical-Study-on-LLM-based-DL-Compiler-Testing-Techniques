import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
eigen_values = torch.linalg.eigvalsh(input_data)