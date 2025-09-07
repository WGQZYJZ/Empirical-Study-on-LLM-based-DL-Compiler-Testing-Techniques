import torch
from torch import nn
from torch.autograd import Variable

input_data = [True, False, True, True]
bool_storage = torch.BoolStorage(input_data)