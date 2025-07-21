import torch
from torch import nn
from torch.autograd import Variable
input_size = (1, 3, 224, 224)
torch.set_num_interop_threads(1)
input_tensor = torch.randn(input_size)