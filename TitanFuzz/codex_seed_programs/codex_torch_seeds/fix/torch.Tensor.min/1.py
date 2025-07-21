'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.min\ntorch.Tensor.min(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
min_value = input_tensor.min()
print(min_value)
min_value = input_tensor.min(dim=1)
print(min_value)
min_value = input_tensor.min(dim=1, keepdim=True)
print(min_value)