import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 2)
torch.onnx.is_in_onnx_export()