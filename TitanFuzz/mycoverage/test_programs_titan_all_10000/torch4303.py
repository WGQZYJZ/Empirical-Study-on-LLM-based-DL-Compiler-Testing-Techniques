import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 1, 224, 224)
torch.inference_mode(mode=True)