'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 3, 2)
print(input_tensor.ndimension())