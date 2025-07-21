'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(2, 3)
_input_tensor = input_tensor.dequantize()
print(_input_tensor)