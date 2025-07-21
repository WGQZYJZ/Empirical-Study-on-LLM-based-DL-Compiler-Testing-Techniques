import torch
from torch import nn
from torch.autograd import Variable
input_data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
half_storage = torch.HalfStorage(input_data)