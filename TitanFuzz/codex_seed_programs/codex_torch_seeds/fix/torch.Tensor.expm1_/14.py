'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1_\ntorch.Tensor.expm1_(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
print('Input Tensor: ', input_tensor)
torch.Tensor.expm1_(input_tensor)
print('Output Tensor: ', input_tensor)