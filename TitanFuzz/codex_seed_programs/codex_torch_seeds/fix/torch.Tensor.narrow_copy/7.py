'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.narrow_copy(_input_tensor, 1, 0, 2)
print(_output_tensor)