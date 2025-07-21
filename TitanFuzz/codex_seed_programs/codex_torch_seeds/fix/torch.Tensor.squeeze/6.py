'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, dim=None)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 3, 1)
squeezed_tensor = input_tensor.squeeze()
print('input_tensor =', input_tensor)
print('squeezed_tensor =', squeezed_tensor)