import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 224, 224)
torch.inference_mode(mode=True)
output_data = torch.randn(1, 1, 224, 224)
torch.inference_mode(mode=False)