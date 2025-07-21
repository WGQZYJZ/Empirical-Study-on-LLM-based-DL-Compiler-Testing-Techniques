'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
mask = torch.tensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=torch.uint8)
result = torch.Tensor.sparse_mask(input_tensor, mask)
print(result)