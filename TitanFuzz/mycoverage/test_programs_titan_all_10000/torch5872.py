import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
dlpack_tensor = torch.utils.dlpack.to_dlpack(x)