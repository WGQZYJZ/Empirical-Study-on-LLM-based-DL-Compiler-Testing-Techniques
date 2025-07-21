'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.signbit\ntorch.Tensor.signbit(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
_output = torch.Tensor.signbit(_input_tensor)
print(_output)