'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma\ntorch.Tensor.lgamma(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.lgamma(_input_tensor)
print(_output_tensor)