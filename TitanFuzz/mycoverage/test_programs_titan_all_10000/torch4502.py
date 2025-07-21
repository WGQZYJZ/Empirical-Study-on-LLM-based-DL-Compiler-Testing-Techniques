import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[0.1, 0.2, 0.3], [0.2, 0.3, 0.4], [0.3, 0.4, 0.5]])
output_data = torch.nonzero(input_data)