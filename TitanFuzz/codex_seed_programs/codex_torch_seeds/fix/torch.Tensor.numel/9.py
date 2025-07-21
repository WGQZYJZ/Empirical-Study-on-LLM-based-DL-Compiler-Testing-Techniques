'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numel\ntorch.Tensor.numel(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 4, 5)
print('input_tensor.numel() = ', input_tensor.numel())