'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dot\ntorch.Tensor.dot(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(3, 4)
other_tensor = torch.randn(4, 5)
_output_tensor = torch.Tensor.dot(_input_tensor, other_tensor)
print(_output_tensor)