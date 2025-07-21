'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log10\ntorch.Tensor.log10(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.log10(_input_tensor)
print(_output_tensor)