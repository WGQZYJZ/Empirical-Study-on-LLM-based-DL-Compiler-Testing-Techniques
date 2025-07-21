import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
rank = torch.linalg.matrix_rank(input_data)