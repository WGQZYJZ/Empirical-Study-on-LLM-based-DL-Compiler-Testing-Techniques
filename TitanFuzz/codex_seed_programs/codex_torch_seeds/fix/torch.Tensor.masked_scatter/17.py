'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, tensor)\n'
import torch
input_tensor = torch.randn(5, 3)
mask = torch.tensor([[1, 0, 1], [0, 0, 1], [1, 1, 1], [0, 1, 0], [1, 1, 0]], dtype=torch.bool)
tensor = torch.randn(5, 3)
result = torch.Tensor.masked_scatter(input_tensor, mask, tensor)
print(result)