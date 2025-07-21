'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.maximum\ntorch.Tensor.maximum(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
_output_tensor = torch.Tensor.maximum(_input_tensor, other)
print(_output_tensor)