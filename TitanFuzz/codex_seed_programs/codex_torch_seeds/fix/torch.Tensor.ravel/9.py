'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
print(torch.Tensor.ravel(input_tensor))