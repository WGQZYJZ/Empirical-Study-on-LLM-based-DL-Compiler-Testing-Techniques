'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze_\ntorch.Tensor.unsqueeze_(_input_tensor, dim)\n'
import torch
input_tensor = torch.rand(1, 3, 3)
print('Input Tensor: ', input_tensor)
output_tensor = torch.unsqueeze(input_tensor, dim=2)
print('Output Tensor: ', output_tensor)
output_tensor = input_tensor.unsqueeze_(dim=2)
print('Output Tensor: ', output_tensor)