import torch
from torch import nn
from torch.autograd import Variable
tensor = torch.rand(2, 3)
dlpack = torch.utils.dlpack.to_dlpack(tensor)