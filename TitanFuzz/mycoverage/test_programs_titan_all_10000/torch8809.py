import torch
from torch import nn
from torch.autograd import Variable
X = torch.randn(3, 3)
X_quantized = torch.quantize_per_tensor(X, 0.5, 0, torch.quint8)
X_dequantized = X_quantized.dequantize()