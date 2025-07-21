'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos_\ntorch.Tensor.arccos_(_input_tensor)\n'
import torch
input_data = torch.randn(1, 3)
print('Input data is: ', input_data)
output = torch.Tensor.arccos_(input_data)
print('Output data is: ', output)