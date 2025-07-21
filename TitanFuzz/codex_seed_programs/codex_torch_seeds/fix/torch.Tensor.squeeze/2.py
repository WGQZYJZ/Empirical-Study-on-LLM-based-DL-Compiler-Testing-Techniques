'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, dim=None)\n'
import torch
input_tensor = torch.randn(1, 2, 1, 3)
print(torch.Tensor.squeeze(input_tensor))
print(torch.Tensor.squeeze(input_tensor, dim=0))
print(torch.Tensor.squeeze(input_tensor, dim=1))
print(torch.Tensor.squeeze(input_tensor, dim=2))
print(torch.Tensor.squeeze(input_tensor, dim=3))