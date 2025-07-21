'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach_\ntorch.Tensor.detach_(_input_tensor, )\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = input_tensor.detach_()
print('The output tensor is: ', output_tensor)
print('The input tensor is: ', input_tensor)