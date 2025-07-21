'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, dim=None)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 1)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.squeeze(input_tensor, dim=3)
print('output_tensor: ', output_tensor)