'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4)
print('input tensor: ', input_tensor)
output_tensor = torch.Tensor.moveaxis(input_tensor, 1, 2)
print('output tensor: ', output_tensor)