'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.zero_\ntorch.Tensor.zero_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
_input_tensor.zero_()
print(_input_tensor)