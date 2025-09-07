import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([0.9, 0.4, 0.2, 0.3, 0.7, 0.1, 0.8, 0.5])
output_data = torch.round(input_data)