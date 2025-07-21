import torch
from torch import nn
from torch.autograd import Variable
data = Variable(torch.randn(1, 1, 1, 1))
torch.is_inference_mode_enabled()