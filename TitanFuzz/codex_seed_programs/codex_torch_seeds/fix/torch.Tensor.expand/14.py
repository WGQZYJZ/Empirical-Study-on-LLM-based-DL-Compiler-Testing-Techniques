'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
print(torch.Tensor.expand(input_tensor, 4, 3))
print(torch.Tensor.expand(input_tensor, 4, 3, 2))
print(torch.Tensor.expand(input_tensor, 4, 3, 2, 1))
print(input_tensor.expand(4, 3))
print(input_tensor.expand(4, 3, 2))
print(input_tensor.expand(4, 3, 2, 1))