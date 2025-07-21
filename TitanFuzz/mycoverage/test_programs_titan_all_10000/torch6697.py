import torch
from torch import nn
from torch.autograd import Variable
input_data = [True, False, True, False]
output_data = torch.BoolStorage(input_data)