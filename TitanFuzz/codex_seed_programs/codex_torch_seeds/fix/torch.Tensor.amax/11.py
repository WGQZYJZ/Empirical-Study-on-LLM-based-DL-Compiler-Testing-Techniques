'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amax\ntorch.Tensor.amax(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 4)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.amax(input_tensor, dim=1, keepdim=False)
print('output_tensor: ', output_tensor)