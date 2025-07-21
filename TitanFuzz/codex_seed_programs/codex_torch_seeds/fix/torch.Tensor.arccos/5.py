'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos\ntorch.Tensor.arccos(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(1, 3)
print('Input Tensor : ', input_tensor)
output_tensor = torch.Tensor.arccos(input_tensor)
print('Output Tensor : ', output_tensor)