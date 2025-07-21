'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rad2deg\ntorch.Tensor.rad2deg(_input_tensor)\n'
import torch
_input_tensor = torch.rand(5, 3)
_output_tensor = _input_tensor.rad2deg()
print(_output_tensor)