'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
result = torch.Tensor.isinf(input_tensor)
print(result)