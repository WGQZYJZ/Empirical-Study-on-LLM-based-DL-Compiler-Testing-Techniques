'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp_\ntorch.Tensor.clamp_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(2, 2)
print('The input tensor is:', input_tensor)
output_tensor = input_tensor.clamp_(min=0)
print('The output tensor is:', output_tensor)