'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.smm\ntorch.Tensor.smm(_input_tensor, mat)\n'
import torch
_input_tensor = torch.randn(3, 4)
mat = torch.randn(4, 5)
_output_tensor = torch.Tensor.smm(_input_tensor, mat)
print(_output_tensor)