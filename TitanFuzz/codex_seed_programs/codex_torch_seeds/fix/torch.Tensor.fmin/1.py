'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fmin\ntorch.Tensor.fmin(_input_tensor, other)\n'
import torch
input_data = torch.rand(10, 3)
min_value = input_data.fmin(dim=1)
print('min_value: ', min_value)