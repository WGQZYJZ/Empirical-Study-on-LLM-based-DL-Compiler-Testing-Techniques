import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 224, 224)
torch.inference_mode(mode=True)
torch.inference_mode(mode=False)
torch.inference_mode(mode=True)
torch.inference_mode(mode=False)