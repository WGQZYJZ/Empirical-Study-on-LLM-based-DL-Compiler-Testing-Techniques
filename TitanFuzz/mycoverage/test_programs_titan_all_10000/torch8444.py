import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange((- 2), 3)
torch.Tensor.square_(input_data)