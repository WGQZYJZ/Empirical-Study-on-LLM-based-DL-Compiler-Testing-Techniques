'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul\ntorch.Tensor.mul(_input_tensor, value)\n'
import torch
_input_tensor = torch.randn(4, 4)
result = torch.Tensor.mul(_input_tensor, 2)
print(result)