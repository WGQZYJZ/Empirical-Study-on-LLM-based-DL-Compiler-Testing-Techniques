'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad\ntorch.Tensor.requires_grad(_input_tensor, )\n'
import torch
input_tensor = torch.rand(10, 10)
result = torch.Tensor.requires_grad(input_tensor, True)
print(result)