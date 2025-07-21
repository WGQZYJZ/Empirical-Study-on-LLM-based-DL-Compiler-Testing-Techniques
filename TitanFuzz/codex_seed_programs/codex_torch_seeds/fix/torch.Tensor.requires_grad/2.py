'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad\ntorch.Tensor.requires_grad(_input_tensor, )\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
output_tensor = torch.Tensor.requires_grad(input_tensor, True)
print(output_tensor)