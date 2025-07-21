'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp\ntorch.Tensor.lerp(_input_tensor, end, weight)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
end = torch.tensor([[10, 20, 30], [40, 50, 60]], dtype=torch.float32)
weights = torch.tensor([0.1, 0.2, 0.3, 0.4], dtype=torch.float32)
print('Task 2: Generate input data')
print('input_tensor: ', input_tensor)
print('end: ', end)
print('weights: ', weights)
print('Task 3: Call the API torch.Tensor.lerp')
print('torch.Tensor.lerp(input_tensor, end, weights): ', torch.Tensor.lerp(input_tensor, end, weights))