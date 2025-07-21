'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exp\ntorch.Tensor.exp(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
_output_tensor = _input_tensor.exp()
print(_output_tensor)