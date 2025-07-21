'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dim\ntorch.Tensor.dim(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
print(_input_tensor.dim())