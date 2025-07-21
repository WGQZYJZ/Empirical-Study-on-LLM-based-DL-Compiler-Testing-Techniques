import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5, 3)
torch.use_deterministic_algorithms(mode=True)