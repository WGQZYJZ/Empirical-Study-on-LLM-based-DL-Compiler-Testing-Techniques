import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3, 224, 224)
torch.use_deterministic_algorithms(True)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False