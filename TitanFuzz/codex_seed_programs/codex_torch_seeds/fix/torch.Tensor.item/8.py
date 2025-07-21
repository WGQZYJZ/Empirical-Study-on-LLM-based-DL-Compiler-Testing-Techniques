'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.item\ntorch.Tensor.item(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1)
_output_tensor = _input_tensor.item()
print(_output_tensor)