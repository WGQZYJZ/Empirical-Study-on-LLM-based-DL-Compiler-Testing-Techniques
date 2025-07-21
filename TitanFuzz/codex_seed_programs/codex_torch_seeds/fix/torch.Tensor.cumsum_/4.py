'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum_\ntorch.Tensor.cumsum_(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(5, 5))
print('input_tensor:', input_tensor)
cum_sum_tensor = torch.zeros_like(input_tensor)
cum_sum_tensor.cumsum_(input_tensor, dim=0)
print('cum_sum_tensor:', cum_sum_tensor)