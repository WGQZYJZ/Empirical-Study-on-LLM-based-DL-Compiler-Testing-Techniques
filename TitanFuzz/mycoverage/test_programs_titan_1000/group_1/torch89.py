import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 2, 2)
torch.is_inference_mode_enabled()