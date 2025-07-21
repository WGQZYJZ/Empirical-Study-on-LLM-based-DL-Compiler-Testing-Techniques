import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
torch.is_inference_mode_enabled()