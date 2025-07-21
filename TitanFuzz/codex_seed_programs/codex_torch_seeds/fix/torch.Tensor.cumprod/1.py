'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod\ntorch.Tensor.cumprod(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randn(4, 3)
cumprod_tensor = input_tensor.cumprod(dim=1, dtype=torch.float)
print('The input tensor: \n', input_tensor)
print('The cumprod tensor: \n', cumprod_tensor)