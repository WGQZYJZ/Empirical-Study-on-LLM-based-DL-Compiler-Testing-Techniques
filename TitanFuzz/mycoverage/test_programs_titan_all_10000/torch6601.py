import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 10)
torch.nn.utils.clip_grad_norm_(input_data, max_norm=1.0, norm_type=2.0, error_if_nonfinite=True)