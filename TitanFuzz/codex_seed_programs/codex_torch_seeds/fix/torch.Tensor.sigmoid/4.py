'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sigmoid\ntorch.Tensor.sigmoid(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.sigmoid(_input_tensor)
print(_output_tensor)