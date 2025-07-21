import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([0.5, 1.0, 1.5, 2.0])
arctan_output = torch.arctan(input_data)