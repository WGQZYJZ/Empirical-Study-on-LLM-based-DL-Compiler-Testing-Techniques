import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
dlpack_input_data = torch.utils.dlpack.to_dlpack(input_data)