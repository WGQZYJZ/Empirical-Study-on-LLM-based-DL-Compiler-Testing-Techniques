'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acos_\ntorch.Tensor.acos_(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3)
print('Input is: ', input_tensor)
torch.Tensor.acos_(input_tensor)
print('Output is: ', input_tensor)