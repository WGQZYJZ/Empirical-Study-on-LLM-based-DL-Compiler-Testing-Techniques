'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
from torch import nn
from torch.quantization import QuantStub, DeQuantStub
import torch.nn.functional as F
input_tensor = torch.randn(2, 3, 4, 5)
torch.Tensor.dequantize(input_tensor)
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor, scale=0.5, zero_point=1)\n'
import torch
from torch import nn
from torch.quantization import QuantStub, DeQuantStub
import torch.nn.functional as F
input_tensor = torch.randn(2, 3, 4, 5)