import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[[True, False], [False, True]], [[True, True], [False, False]]])
output = torch.logical_not(input_data)