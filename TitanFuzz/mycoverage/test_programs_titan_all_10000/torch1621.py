import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 3, 4)
torch.set_num_interop_threads(2)