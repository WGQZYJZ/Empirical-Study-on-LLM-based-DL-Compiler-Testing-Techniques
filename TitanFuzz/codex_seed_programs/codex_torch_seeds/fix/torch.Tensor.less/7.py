'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less\ntorch.Tensor.less(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.less(0.5)
print('output_tensor: ', output_tensor)