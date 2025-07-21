import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
device_id = torch.Tensor.get_device(input_data)