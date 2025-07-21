'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
from torch import Tensor
from torch.quantization import QuantStub, DeQuantStub
print(torch.__version__)
input_tensor = Tensor([0, 1, 2, 3])
dequantized_tensor = torch.Tensor.dequantize(input_tensor)
print(dequantized_tensor)