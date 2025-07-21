'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_meta\ntorch.Tensor.is_meta(_input_tensor, )\n'
import torch
input_tensor = torch.rand(2, 3)
result = torch.Tensor.is_meta(input_tensor)
print('result: ', result)