'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4, requires_grad=True)
print('input_tensor: ', input_tensor)
input_tensor.retain_grad()
print('input_tensor.retain_grad(): ', input_tensor.retain_grad())