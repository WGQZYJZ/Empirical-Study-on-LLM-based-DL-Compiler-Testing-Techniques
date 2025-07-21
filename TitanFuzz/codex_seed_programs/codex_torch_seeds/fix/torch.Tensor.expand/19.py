'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.rand(2, 3)
output_tensor = input_tensor.expand(2, 3, 4)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)