'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eq\ntorch.Tensor.eq(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
result = torch.Tensor.eq(input_tensor, other)
print(result)