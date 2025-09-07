import torch
from torch import nn
from torch.autograd import Variable

x = Variable(torch.randn(1, 3, 224, 224))
torch.onnx.is_in_onnx_export()
x = Variable(torch.randn(1, 3, 224, 224))
torch