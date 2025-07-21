'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.angle\ntorch.Tensor.angle(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print(_input_tensor)
print(torch.Tensor.angle(_input_tensor))