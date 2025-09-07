import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(4, 3, 224, 224)
dlpack_data = torch.utils.dlpack.to_dlpack(input_data)