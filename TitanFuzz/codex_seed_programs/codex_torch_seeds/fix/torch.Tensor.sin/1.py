'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sin\ntorch.Tensor.sin(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.sin(_input_tensor)
print(_input_tensor)
print(_output_tensor)