'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
output = input_tensor.any(dim=1, keepdim=True)
print(output)