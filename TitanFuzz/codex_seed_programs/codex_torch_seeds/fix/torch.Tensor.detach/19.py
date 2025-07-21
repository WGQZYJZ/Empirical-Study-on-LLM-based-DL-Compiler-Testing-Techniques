'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
import torch
input_tensor = torch.randn((3, 5), requires_grad=True)
output_tensor = input_tensor.detach()
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)