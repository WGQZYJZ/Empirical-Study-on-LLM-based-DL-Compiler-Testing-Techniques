'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod\ntorch.Tensor.cumprod(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randn(1, 3, 4, 5)
print('Input tensor: ', input_tensor)
cum_prod_tensor = input_tensor.cumprod(dim=3)
print('Cumulative product tensor: ', cum_prod_tensor)