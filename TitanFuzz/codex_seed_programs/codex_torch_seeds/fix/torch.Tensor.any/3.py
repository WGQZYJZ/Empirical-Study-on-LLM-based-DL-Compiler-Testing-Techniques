'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print('The input tensor is:', input_tensor)
output_tensor = input_tensor.any(dim=1, keepdim=True)
print('The output tensor is:', output_tensor)