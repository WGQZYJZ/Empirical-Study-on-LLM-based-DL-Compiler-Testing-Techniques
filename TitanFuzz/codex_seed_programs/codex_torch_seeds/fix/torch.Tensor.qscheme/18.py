'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
import torch.quantization
input_tensor = torch.rand(2, 3, dtype=torch.float)
print('Input tensor = ', input_tensor)
qscheme = input_tensor.qscheme()
print('qscheme = ', qscheme)