'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3)
result = input_tensor.is_floating_point()
print(result)