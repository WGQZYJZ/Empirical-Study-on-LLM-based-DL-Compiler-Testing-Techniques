'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lt\ntorch.Tensor.lt(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
print(input_tensor.lt(0.5))