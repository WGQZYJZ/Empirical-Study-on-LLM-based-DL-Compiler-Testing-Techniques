'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum_\ntorch.Tensor.cumsum_(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.randn(1, 3, 4, 5)
print('input_tensor: ', input_tensor)
print('input_tensor.size(): ', input_tensor.size())
input_tensor.cumsum_(dim=1, dtype=torch.float32)
print('input_tensor.size(): ', input_tensor.size())
print('input_tensor: ', input_tensor)