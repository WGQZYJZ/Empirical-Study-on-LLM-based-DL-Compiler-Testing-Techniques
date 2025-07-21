'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.randn(1, 3, 7, 7)
output_tensor = input_tensor.expand(2, 3, 7, 7)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)