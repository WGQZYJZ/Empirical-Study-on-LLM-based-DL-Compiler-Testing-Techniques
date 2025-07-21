'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndim\ntorch.Tensor.ndim(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
print(torch.Tensor.ndim(input_tensor))