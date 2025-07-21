'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isnan\ntorch.Tensor.isnan(_input_tensor)\n'
import torch
_input_tensor = torch.randn(10, 10)
_input_tensor[(0, 0)] = float('nan')
print(torch.Tensor.isnan(_input_tensor))