'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gt\ntorch.Tensor.gt(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
result = input_tensor.gt(0)
print(result)