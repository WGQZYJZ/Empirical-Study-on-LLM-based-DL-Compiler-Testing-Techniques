import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(low=0, high=10, size=(5, 5))
output_data = torch.randint(low=0, high=10, size=(5, 5))