'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(10, 3)
print(input_tensor)
cummin_result = input_tensor.cummin(dim=0)
print(cummin_result)