'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, *shape)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 3)
output_tensor = input_tensor.view(9)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)