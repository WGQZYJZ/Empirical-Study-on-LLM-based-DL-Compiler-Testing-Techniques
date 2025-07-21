'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.i0\ntorch.Tensor.i0(_input_tensor)\n'
import torch
_input_tensor = torch.rand(10, 10)
_output_tensor = torch.Tensor.i0(_input_tensor)
print(_output_tensor)